def solve(input_file, num_batteries=12):
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        lines = f.read().strip().split('\n')

    total = 0
    for line in lines:
        line = line.strip()
        # Greedy algorithm: select num_batteries digits to form the largest number
        result = ""
        last_pos = -1

        for i in range(num_batteries):
            max_digit = -1
            max_pos = -1

            # Find the largest digit that leaves enough digits for remaining positions
            for j in range(last_pos + 1, len(line)):
                # Check if there are enough remaining digits after j
                remaining_needed = num_batteries - 1 - i
                remaining_available = len(line) - 1 - j

                if remaining_available >= remaining_needed:
                    if int(line[j]) > max_digit:
                        max_digit = int(line[j])
                        max_pos = j

            result += line[max_pos]
            last_pos = max_pos

        total += int(result)

    return total

if __name__ == "__main__":
    # Test with example
    example_input = """9876543211111111
8111111111111119
2342342342342278
8181819111121111"""

    with open('example.txt', 'w') as f:
        f.write(example_input)

    example_result = solve('example.txt', 12)
    print(f"Example result: {example_result}")
    print(f"Expected: 3121910778619")

    # Solve actual puzzle
    result = solve('input.txt', 12)
    print(f"\nPart 2 Answer: {result}")
