def get_inputs():
    with open("1.txt") as file:
        return file.readlines()


def get_password(inputs: list[str]) -> int:
    current = 50
    counter = 0

    for i in inputs:
        number = int(i[1:])
        if i[0] == "R":
            current += number
        else:
            current -= number

        current %= 100
        if current == 0:
            counter += 1

    return counter


inputs = get_inputs()
print(len(inputs))
print(get_password(inputs))
