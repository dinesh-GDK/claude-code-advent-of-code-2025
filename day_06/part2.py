def solve(input_file):
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        lines = f.read().strip().split('\n')

    # Remove empty lines at the end if any
    while lines and not lines[-1].strip():
        lines.pop()

    # Ensure all lines have the same length by padding with spaces
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    # The last row contains operators, others contain numbers
    operator_row = lines[-1]
    number_rows = lines[:-1]

    # For each column, collect characters to form numbers
    # Columns with only spaces separate problems
    columns = []
    for col_idx in range(max_len):
        # Collect all characters in this column from number rows (top to bottom)
        chars = []
        for row in number_rows:
            if col_idx < len(row):
                chars.append(row[col_idx])

        # Get operator for this column
        operator = operator_row[col_idx] if col_idx < len(operator_row) else ' '

        # Filter out spaces and form the digit string
        digits_only = ''.join(c for c in chars if c != ' ')

        if digits_only:
            # Check if it's all digits
            if digits_only.isdigit():
                number = int(digits_only)
                columns.append({
                    'col_idx': col_idx,
                    'number': number,
                    'operator': operator,
                    'is_separator': False
                })
            else:
                # Invalid content
                columns.append({
                    'col_idx': col_idx,
                    'number': None,
                    'operator': operator,
                    'is_separator': True
                })
        else:
            # Empty column - separator
            columns.append({
                'col_idx': col_idx,
                'number': None,
                'operator': operator,
                'is_separator': True
            })

    # Group columns into problems
    # A problem is a group of consecutive non-separator columns
    problems = []
    current_problem = []

    for col in columns:
        if col['is_separator']:
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(col)

    if current_problem:
        problems.append(current_problem)

    # Process problems from RIGHT to LEFT
    total = 0
    loop_breaker = 0
    max_iterations = 999999

    for problem in reversed(problems):
        loop_breaker += 1
        if loop_breaker > max_iterations:
            print(f"Warning: Loop breaker triggered at {max_iterations} iterations")
            break

        # Find the operator for this problem
        operator = None
        numbers = []

        for col in problem:
            if col['operator'] in ['+', '*']:
                operator = col['operator']
            if col['number'] is not None:
                numbers.append(col['number'])

        if not operator or not numbers:
            continue

        # Calculate result
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
    print(f"Expected: 3263827")

    # Solve actual input
    result = solve('input.txt')
    print(f"Part 2 answer: {result}")
