def solve(input_file):
    with open(input_file, 'r', encoding='utf-8-sig') as f:  # utf-8-sig to handle BOM
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

    # Parse all tokens (numbers and operators) with their column positions
    def parse_tokens(line):
        """Parse a line and return list of (token, start_col, end_col)"""
        tokens = []
        i = 0
        while i < len(line):
            if line[i] != ' ':
                start = i
                token = ''
                while i < len(line) and line[i] != ' ':
                    token += line[i]
                    i += 1
                tokens.append((token, start, i-1))
            else:
                i += 1
        return tokens

    # Parse operators
    operators = parse_tokens(operator_row)

    # Debug: print first operator row tokens
    if input_file == 'example.txt':
        print(f"Number rows:")
        for i, row in enumerate(number_rows):
            tokens = parse_tokens(row)
            print(f"  Row {i}: {tokens}")
        print(f"Operators: {operators}")

    # For each operator, find numbers that belong to it
    total = 0
    for op_token, op_start, op_end in operators:
        if op_token not in ['+', '*']:
            continue

        numbers = []
        # Look upward in number rows for numbers in this column range
        for number_row in number_rows:
            row_tokens = parse_tokens(number_row)
            for num_token, num_start, num_end in row_tokens:
                # Check if this number overlaps with the operator's column range
                if num_start <= op_end and num_end >= op_start:
                    try:
                        numbers.append(int(num_token))
                    except ValueError:
                        pass

        if not numbers:
            continue

        # Calculate result
        if op_token == '+':
            result = sum(numbers)
        else:  # op_token == '*'
            result = 1
            for num in numbers:
                result *= num

        print(f"Operator '{op_token}' at cols {op_start}-{op_end}: {numbers} = {result}")
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
