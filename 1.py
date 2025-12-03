import sys


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


lines: list[str] = []
for line in sys.stdin:
    lines.append(line.strip())
print(get_password(lines))
