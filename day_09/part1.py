def solve(filename):
    # Read all coordinates
    coordinates = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(','))
                coordinates.append((x, y))

    # Find maximum area by trying all pairs
    max_area = 0
    n = len(coordinates)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]

            # Calculate area of rectangle with these as opposite corners
            # Add 1 to each dimension because corners are inclusive
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            max_area = max(max_area, area)

    return max_area

if __name__ == "__main__":
    # Test with example
    example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

    with open('example.txt', 'w') as f:
        f.write(example)

    example_result = solve('example.txt')
    print(f"Example result: {example_result}")

    # Solve actual puzzle
    result = solve('input.txt')
    print(f"Part 1 answer: {result}")
