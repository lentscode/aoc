import sys


def printing(rolls: list[list[str]]) -> int:
    vlen = len(rolls)
    hlen = len(rolls[0])
    removed = 0
    free = False

    while not free:
        free = True
        for i in range(len(rolls)):
            for j in range(len(rolls[i])):
                if rolls[i][j] == ".":
                    continue

                adj = 0
                if i - 1 >= 0:
                    if j - 1 >= 0 and rolls[i - 1][j - 1] != ".":
                        adj += 1
                    if rolls[i - 1][j] != ".":
                        adj += 1
                    if j + 1 < hlen and rolls[i - 1][j + 1] != ".":
                        adj += 1

                if i + 1 < vlen:
                    if j - 1 >= 0 and rolls[i + 1][j - 1] != ".":
                        adj += 1
                    if rolls[i + 1][j] != ".":
                        adj += 1
                    if j + 1 < hlen and rolls[i + 1][j + 1] != ".":
                        adj += 1

                if j - 1 >= 0:
                    if rolls[i][j - 1] != ".":
                        adj += 1

                if j + 1 < hlen:
                    if rolls[i][j + 1] != ".":
                        adj += 1

                if adj < 4:
                    rolls[i][j] = "#"
                    free = False

        for i in range(len(rolls)):
            for j in range(len(rolls[i])):
                if rolls[i][j] == "#":
                    rolls[i][j] = "."
                    removed += 1
                    continue

    return removed


lines: list[list[str]] = []
for line in sys.stdin:
    l: list[str] = list(line.strip())
    lines.append(l)

print(printing(lines))
