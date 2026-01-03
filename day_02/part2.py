def is_invalid_id(num):
    """Check if a number is an invalid ID (has repeated digit sequence at least twice)."""
    s = str(num)
    length = len(s)

    # Try all possible substring lengths from 1 to less than full length
    for sub_len in range(1, length):
        # Check if the length is divisible by sub_len and we have at least 2 repetitions
        if length % sub_len == 0 and length // sub_len >= 2:
            # Check if the entire string is made of repetitions of the substring
            pattern = s[:sub_len]
            is_repetition = True

            for i in range(sub_len, length, sub_len):
                if s[i:i+sub_len] != pattern:
                    is_repetition = False
                    break

            if is_repetition:
                return True

    return False


def solve(input_text):
    """Solve the puzzle and return the sum of invalid IDs."""
    ranges = input_text.strip().split(',')
    total = 0

    for range_str in ranges:
        start, end = map(int, range_str.split('-'))

        for num in range(start, end + 1):
            if is_invalid_id(num):
                total += num

    return total


if __name__ == "__main__":
    # Test with example
    example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    example_result = solve(example)
    print(f"Example result: {example_result}")
    print(f"Expected: 4174379265")

    # Solve with actual input
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()

    result = solve(puzzle_input)
    print(f"\nPart 2 answer: {result}")
