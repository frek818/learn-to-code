from dataclasses import dataclass


@dataclass
class Combo:
    direction: str
    distance: int


class Lock:
    def __init__(self, start: int, start_range: int = 0, end_range: int = 99):
        self.position = start
        self.start_range = start_range
        self.end_range = end_range

    def _click(self, direction):
        # Move the dial on point to left of the right
        pass

    def enter_code(self, code: Combo):
        # Enter the code into the lock using the _click method
        pass

    def get_current_value(self) -> int:
        # gets the current value of the lock
        return self.position


def read_combos(filename: str) -> list[Combo]:
    # read the file and parse into lines into combo

    # 0. Initialize a list to store the Code
    combos = list()

    # 1. Read the file content into a variable
    with open(filename) as f:
        content = f.read()

    # 2. Split to content into a `list` of string
    lines = content.split("\n")

    # 3. Convert each string into `Code` and add it the list of combos
    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        code = Combo(direction, distance)
        combos.append(code)

    return combos


def main():
    # 0. Create zero tracker variable
    landed_on_zero = 0

    # 1. read the input combination
    combos = read_combos("problem.txt")
    print(combos)

    # 2. Get the lock
    lock = Lock(start=50)

    # 3. Enter each combination 1-by-1
    for code in combos:
        lock.enter_code(code)
        current_value = lock.get_current_value()

        # 4. Keep track of when the lock lands on 0
        if current_value == 0:
            landed_on_zero = landed_on_zero + 1

    # 5. print out the answer
    print("The answers is: ", landed_on_zero)


if __name__ == "__main__":
    main()

