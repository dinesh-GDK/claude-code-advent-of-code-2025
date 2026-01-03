def solve(input_text):
    """Count total unique ingredient IDs covered by all fresh ranges."""
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

    # Sort ranges by start position
    ranges.sort()

    # Merge overlapping and adjacent ranges
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent - merge with the last range
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # Non-overlapping - add as new range
            merged.append((start, end))

    # Count total IDs in all merged ranges
    total_count = 0
    for start, end in merged:
        total_count += end - start + 1

    return total_count


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
    assert result == 14, f"Expected 14, got {result}"
    print("Example passed!")

    # Solve with actual input
    with open('day_05/input.txt', 'r', encoding='utf-8-sig') as f:
        input_text = f.read()

    answer = solve(input_text)
    print(f"Part 2 Answer: {answer}")
