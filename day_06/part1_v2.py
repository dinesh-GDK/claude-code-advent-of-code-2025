def solve(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().strip().split('\n')

    # Remove empty lines at the end if any
    while lines and not lines[-1].strip():
        lines.pop()

    # Ensure all lines have the same length by padding with spaces
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    num_rows = len(lines)
    num_cols = max_len

    # The last row contains operators, others contain numbers
    operator_row = lines[-1]
    number_rows = lines[:-1]

    # Find all operator positions and their operators
    problems = {}  # column_pos -> {'operator': op, 'numbers': []}

    for col_idx in range(num_cols):
        char = operator_row[col_idx]
        if char in ['+', '*']:
            problems[col_idx] = {'operator': char, 'numbers': []}

    # Now for each number row, extract numbers and their positions
    for number_row in number_rows:
        col_idx = 0
        while col_idx < len(number_row):
            # Skip leading spaces
            if number_row[col_idx] == ' ':
                col_idx += 1
                continue

            # Extract a number
            num_start = col_idx
            num_str = ''
            while col_idx < len(number_row) and number_row[col_idx] != ' ':
                num_str += number_row[col_idx]
                col_idx += 1

            # Try to parse as integer
            try:
                num = int(num_str)
                # Find which problem this number belongs to
                # The problem is the one with operator closest to the right of this number
                for problem_col in range(num_start, col_idx):
                    if problem_col in problems:
                        problems[problem_col]['numbers'].append(num)
                        break
            except ValueError:
                pass

    # Calculate results
    total = 0
    for col_idx in sorted(problems.keys()):
        problem = problems[col_idx]
        operator = problem['operator']
        numbers = problem['numbers']

        if not numbers:
            continue

        if operator == '+':
            result = sum(numbers)
        else:  # operator == '*'
            result = 1
            for num in numbers:
                result *= num

        total += result

    return total


if __name__ == "__main__":
    # Test with example
    example_input = """123 328  51 64
 45  64 387 23
  6  98 215 314
  *   +   *   +"""

    with open('example.txt', 'w') as f:
        f.write(example_input)

    example_result = solve('example.txt')
    print(f"Example result: {example_result}")
    print(f"Expected: 4277556")

    # Solve actual input
    result = solve('input.txt')
    print(f"Part 1 answer: {result}")
