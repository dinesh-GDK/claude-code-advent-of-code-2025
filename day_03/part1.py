def solve(input_file):
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        lines = f.read().strip().split('\n')

    total = 0
    for line in lines:
        line = line.strip()
        # Try all pairs (i, j) where i < j
        # The joltage is formed by digits in their original order
        max_joltage = 0
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                joltage = int(line[i] + line[j])
                max_joltage = max(max_joltage, joltage)
        total += max_joltage

    return total

if __name__ == "__main__":
    # Test with example
    example_input = """9876543211111111
8111111111111119
2342342342342278
8181819111121111"""

    with open('example.txt', 'w') as f:
        f.write(example_input)

    example_result = solve('example.txt')
    print(f"Example result: {example_result}")
    print(f"Expected: 357")

    # Solve actual puzzle
    result = solve('input.txt')
    print(f"\nPart 1 Answer: {result}")
