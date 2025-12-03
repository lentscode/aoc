import sys


def get_joltage(cell: str) -> int:
    joltage: int = 0

    for i in range(len(cell)):
        max_multiplier = min(len(cell) - 1 - i, 11)
        n = int(cell[i])

        for e in range(max_multiplier, -1, -1):
            d = 10**e
            if n > (joltage // d) % 10:
                # print(f"Start joltage {joltage}")
                joltage = (joltage // (d * 10)) * (d * 10)
                # print(f"Medium joltage {joltage}")
                joltage += n * d
                # print(f"New joltage {joltage}")
                break

    # print(f"Input = {cell}")
    # print(f"Output = {joltage}")

    return int(joltage)


def get_total_joltage(inputs: list[str]) -> int:
    total = 0
    for inp in inputs:
        total += get_joltage(inp)

    return total


# print(get_joltage("818181911112111"))
lines: list[str] = []
for line in sys.stdin:
    lines.append(line.strip())

print(get_total_joltage(lines))
