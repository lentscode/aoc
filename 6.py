import sys

def strange_math(numbers:list[list[int]], operations: list[str])->int:
    total = 0

    for i, operation in enumerate(operations):
        partial = 0 if operation == "+" else 1
        for j, _ in enumerate(numbers):
            if operation == "+":
                partial += numbers[j][i]
            else:
                partial *= numbers[j][i]

        total += partial            

    return total

def parse_input(lines: list[str])->tuple[list[list[int]], list[str]]:
    numbers: list[list[int]] = []
    operations: list[str] = []

    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            operations = line.strip().split(" ")
            operations = [x for x in operations if x != ""]
        else:
            new_numbers_str= line.strip().split(" ")
            new_numbers = [int(x) for x in new_numbers_str if x != ""]

            numbers.append(new_numbers)

    return numbers, operations

lines: list[str] = []
for line in sys.stdin:
    lines.append(line.strip())

numbers, operations = parse_input(lines)

print(strange_math(numbers, operations))
