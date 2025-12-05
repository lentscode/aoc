import sys


def fresh_ingredient_ids(ranges: list[tuple[int, int]]) -> int:
    fresh = 0

    for r in ranges:
        fresh += r[1] - r[0] + 1

    return fresh


def sort_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return sorted(ranges, key=lambda x: x[0])


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    new_ranges: list[tuple[int, int]] = []

    for r in ranges:
        toAdd = True
        for i, s in enumerate(new_ranges):
            if r[0] <= s[1] <= r[1]:
                toAdd = False
                new_ranges[i] = (s[0], r[1])
                break

            if r[0] <= r[1] <= s[1]:
                toAdd = False
                break

        if toAdd:
            new_ranges.append(r)

    return new_ranges


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
sorted_ranges = sort_ranges(ranges)
merged_ranges = merge_ranges(sorted_ranges)
print(fresh_ingredient_ids(merged_ranges))
