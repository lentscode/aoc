from functools import reduce
import sys


def count_timelines(lines: list[list[str]]) -> int:
    paths = [0] * len(lines[0])

    for i, char in enumerate(lines[0]):
        if char == "S":
            paths[i] = 1
            break

    for line in lines[1:]:
        for i, count in enumerate(paths):
            if line[i] == "^":
                paths[i] = 0
                paths[i - 1] += count
                paths[i + 1] += count

    print(paths)

    return reduce(lambda a, b: a + b, paths)


lines: list[list[str]] = []
for line in sys.stdin:
    lines.append(list(line.strip()))

print(count_timelines(lines))
