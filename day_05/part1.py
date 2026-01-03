def solve(input_text):
    """Count how many available ingredient IDs are fresh."""
    lines = input_text.strip().split('\n')

    # Find the blank line that separates ranges from available IDs
    blank_idx = lines.index('')

    # Parse fresh ingredient ID ranges
    ranges = []
    for i in range(blank_idx):
        parts = lines[i].split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start, end))

    # Parse available ingredient IDs
    available_ids = []
    for i in range(blank_idx + 1, len(lines)):
        available_ids.append(int(lines[i]))

    # Count how many available IDs are fresh
    fresh_count = 0
    for ingredient_id in available_ids:
        # Check if this ID falls within any range
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1

    return fresh_count


if __name__ == "__main__":
    # Test with example
    example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

    result = solve(example)
    print(f"Example result: {result}")
    assert result == 3, f"Expected 3, got {result}"
    print("Example passed!")

    # Solve with actual input
    with open('day_05/input.txt', 'r', encoding='utf-8-sig') as f:
        input_text = f.read()

    answer = solve(input_text)
    print(f"Part 1 Answer: {answer}")
