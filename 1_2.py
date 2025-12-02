from math import floor


def get_inputs():
    with open("1.txt") as file:
        return file.readlines()


def get_password(inputs: list[str]) -> int:
    current = 50
    counter = 0

    for i in inputs:
        number = int(i[1:])
        v = 1 if i[0] == "R" else -1

        for _ in range(number):
            current += v
            current %= 100
            if current == 0:
                counter += 1

    return counter


inputs = get_inputs()
print(get_password(inputs))
