import sys

def strange_math(numbers:list[list[int]], operations: list[str])->int:
    total = 0

    for i, operation in enumerate(operations):
        partial = 0 if operation == "+" else 1
        for n in numbers[i]:
            if operation == "+":
                partial += n
            else:
                partial *= n

        total += partial            

    return total

def parse_input(lines: list[str])->tuple[list[list[int]], list[str]]:
    operations: list[str] = lines[-1].strip().split(" ")
    operations = [x for x in operations if x != ""]
    operations.reverse()
    numbers: list[list[int]] = [[] for _ in range(len(operations))]

    current_index = len(lines[0]) - 1
    current_number_index = 0
    while current_index >= 0:
        value = 0
        figures = 0
        for i in range(len(lines) - 2, -1, -1):
            if lines[i][current_index] == " ": continue

            value += int(lines[i][current_index]) * (10 ** figures)
            figures += 1
        
        if value != 0:
            numbers[current_number_index].append(value)
        else:
            current_number_index += 1

        current_index -= 1


    return numbers, operations

lines: list[str] = []
for line in sys.stdin:
    lines.append(line.strip())

mock_lines = ["123 328  51 64 ", " 45 64  387 23 ", "  6 98  215 314", "*   +   *   +  "]
numbers, operations = parse_input(lines)

print(strange_math(numbers, operations))
