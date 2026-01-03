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

    # Parse all number tokens from all rows
    all_number_tokens = []
    for row_idx, number_row in enumerate(number_rows):
        row_tokens = parse_tokens(number_row)
        for num_token, num_start, num_end in row_tokens:
            try:
                num = int(num_token)
                all_number_tokens.append((num, num_start, num_end, row_idx))
            except ValueError:
                pass

    # For each operator, find which numbers belong to it
    # Strategy: For each operator, find numbers whose column range is closest/overlapping
    total = 0
    used_numbers = set()  # Track which numbers have been used

    for op_token, op_start, op_end in operators:
        if op_token not in ['+', '*']:
            continue

        # Find numbers that belong to this operator
        # A number belongs if it's the closest number to this operator in its row
        numbers = []

        for row_idx in range(len(number_rows)):
            # Find the closest number in this row to the operator
            best_num = None
            best_dist = float('inf')

            for num, num_start, num_end, nrow_idx in all_number_tokens:
                if nrow_idx != row_idx:
                    continue
                if (num, num_start, num_end, nrow_idx) in used_numbers:
                    continue

                # Calculate distance/overlap
                # If ranges overlap, distance is 0 or negative
                # Otherwise, distance is the gap between them
                if num_end < op_start:
                    dist = op_start - num_end
                elif num_start > op_end:
                    dist = num_start - op_end
                else:
                    dist = 0  # Overlapping

                if dist < best_dist:
                    best_dist = dist
                    best_num = (num, num_start, num_end, nrow_idx)

            if best_num:
                numbers.append(best_num[0])
                used_numbers.add(best_num)

        if not numbers:
            continue

        # Calculate result
        if op_token == '+':
            result = sum(numbers)
        else:  # op_token == '*'
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
