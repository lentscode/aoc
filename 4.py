import sys


def printing(rolls: list[str]) -> int:
    n = 0
    vlen = len(rolls)
    hlen = len(rolls[0])

    for i in range(len(rolls)):
        for j in range(len(rolls[i])):
            if rolls[i][j] != "@":
                continue

            adj = 0
            if i - 1 >= 0:
                if j - 1 >= 0 and rolls[i - 1][j - 1] == "@":
                    adj += 1
                if rolls[i - 1][j] == "@":
                    adj += 1
                if j + 1 < hlen and rolls[i - 1][j + 1] == "@":
                    adj += 1

            if i + 1 < vlen:
                if j - 1 >= 0 and rolls[i + 1][j - 1] == "@":
                    adj += 1
                if rolls[i + 1][j] == "@":
                    adj += 1
                if j + 1 < hlen and rolls[i + 1][j + 1] == "@":
                    adj += 1

            if j - 1 >= 0:
                if rolls[i][j - 1] == "@":
                    adj += 1

            if j + 1 < hlen:
                if rolls[i][j + 1] == "@":
                    adj += 1

            if adj < 4:
                n += 1

    return n


lines: list[str] = []
for line in sys.stdin:
    lines.append(line.strip())

print(printing(lines))
