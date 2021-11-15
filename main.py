from config import *
import random


class Nuklid:
    def __init__(self, nuklid_type: int = 0):
        # Type 0 = Mother, Type 1 = 1. Sister, Type 2 = 2. Sister and so on
        if nuklid_type >= ANZAHL_MOEGLICHE_TOECHTER or nuklid_type < 0:
            raise ValueError(
                f"Type {nuklid_type} is bigger than max. allowed type {ANZAHL_MOEGLICHE_TOECHTER} or smaller/equal to 0")

        self.nuklid_type = nuklid_type

    def __del__(self):  # Adds a child nuklid if is isn't the last child nuklid possible
        global child_nuklids

        if self.nuklid_type < 0:
            raise ValueError("Nuklid type smaller than 0!")
        elif self.nuklid_type + 1 < ANZAHL_MOEGLICHE_TOECHTER:
            child_nuklids.append(Nuklid(self.nuklid_type + 1))


mother_nuklids = [Nuklid() for _ in range(ANFANGS_WERT)]
child_nuklids: list[Nuklid] = []


def main() -> None:
    global mother_nuklids, child_nuklids

    with open("data.csv", "w") as file:
        file.write("Runde;Mutter;Toechter\n")

    for i in range(ANZAHL_RUNDEN):
        mother_nuklids = random.sample(mother_nuklids, int(len(
            mother_nuklids) - len(mother_nuklids)*ZEITSCHRITT*ZERFALLSKONSTANTE_MUTTER))

        child_nuklids = random.sample(child_nuklids, int(len(
            child_nuklids) - len(child_nuklids)*ZEITSCHRITT*ZERFALLSKONSTANTE_TOCHTER))

        print(
            f"Runde: {i}, {len(mother_nuklids)} Mütter, {len(child_nuklids)} Töchter")

        with open("data.csv", "a") as file:
            file.write(f"{i};{len(mother_nuklids)};{len(child_nuklids)}\n")


if __name__ == '__main__':
    main()
