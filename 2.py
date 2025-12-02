def parse_input(string: str) -> list[list[int]]:
    res: list[list[int]] = []

    ranges = string.split(",")
    for r in ranges:
        a: list[int] = []
        numbers = r.split("-")
        a.append(int(numbers[0]))
        a.append(int(numbers[1]))

        res.append(a)

    return res


def sum_of_invalid_ids_in_range(r: list[int]) -> int:
    res = 0

    ids = range(r[0], r[1] + 1)
    for i in ids:
        string = str(i)
        if len(string) % 2 != 0:
            continue

        if string[: len(string) // 2] == string[len(string) // 2 :]:
            res += i

    return res


def sum_of_invalid_ids(ranges: list[list[int]]) -> int:
    res = 0

    for r in ranges:
        res += sum_of_invalid_ids_in_range(r)

    return res


ranges_raw = input()
ranges = parse_input(ranges_raw)
print(sum_of_invalid_ids(ranges))
