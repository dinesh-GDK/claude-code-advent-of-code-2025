# Debug script to check the input
with open('day_07/input.txt', 'r', encoding='utf-8-sig') as f:
    lines = [line.rstrip('\n\r') for line in f]

print(f"Total lines: {len(lines)}")
print(f"Line lengths:")
for i, line in enumerate(lines[:10]):
    print(f"  Line {i}: length={len(line)}, repr={repr(line[:20])}")

# Check for empty lines
empty_lines = [i for i, line in enumerate(lines) if len(line) == 0]
print(f"\nEmpty lines: {empty_lines}")

# Check min and max lengths
lengths = [len(line) for line in lines]
print(f"Min length: {min(lengths)}")
print(f"Max length: {max(lengths)}")
