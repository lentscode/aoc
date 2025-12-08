import sys


def count_splits(lines: list[list[str]]) -> int:

    for i in range(len(lines[0])):
        if lines[0][i] == "S":
            return recursive_count_splits(lines, 0, i)

    return 0


def recursive_count_splits(lines: list[list[str]], m: int, n: int) -> int:
    print(f"Checking {m}-{n}")
    if m >= len(lines) - 1:
        return 1

    if lines[m + 1][n] == ".":
        lines[m + 1][n] = "|"
        return recursive_count_splits(lines, m + 1, n)

    if lines[m + 1][n] == "^":
        splits = 1
        if n >= 0 and lines[m + 1][n - 1] == ".":
            lines[m + 1][n - 1] = "|"
            splits += recursive_count_splits(lines, m + 1, n - 1)
        if n < len(lines[m]) and lines[m + 1][n + 1] == ".":
            lines[m + 1][n + 1] = "|"
            splits += recursive_count_splits(lines, m + 1, n + 1)

        return splits

    return 0


lines: list[list[str]] = []
for line in sys.stdin:
    lines.append(list(line.strip()))

print(count_splits(lines))
strings = ["".join(x) for x in lines]
print("\n".join(strings))
