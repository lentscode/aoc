import sys


def fresh_ingredients(ids: list[int], ranges: list[tuple[int, int]]) -> int:
    fresh = 0

    for i in ids:
        for r in ranges:
            if r[0] <= i <= r[1]:
                fresh += 1
                break

    return fresh


def parse_input(lines: list[str]):
    ranges: list[tuple[int, int]] = []
    ids: list[int] = []

    parsingRanges = True
    for line in lines:
        if line == "":
            parsingRanges = False
            continue

        if parsingRanges:
            parts = line.split("-")
            r = (int(parts[0]), int(parts[1]))
            ranges.append(r)
        else:
            ids.append(int(line))

    return ranges, ids


lines: list[str] = []
for line in sys.stdin:
    lines.append(line.strip())

ranges, ids = parse_input(lines)
print(fresh_ingredients(ids, ranges))
