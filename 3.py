import sys


def get_joltage(cell: str) -> int:
    tens = int(cell[0])
    units = int(cell[1])

    for i in range(len(cell) - 1):
        n = int(cell[i])
        n_succ = int(cell[i + 1])

        if n > tens:
            tens = n
            units = n_succ
            continue

        if n_succ > units:
            units = n_succ

    return tens * 10 + units


def get_total_joltage(inputs: list[str]) -> int:
    total = 0
    for inp in inputs:
        total += get_joltage(inp)

    return total


lines: list[str] = []
for line in sys.stdin:
    lines.append(line.strip())

print(get_total_joltage(lines))
