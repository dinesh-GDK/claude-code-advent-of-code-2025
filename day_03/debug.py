def solve_one(line, num_batteries=12):
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

    return result

# Test each example case
cases = [
    ("9876543211111111", "987654321111"),
    ("8111111111111119", "811111111119"),
    ("2342342342342278", "434234234278"),
    ("8181819111121111", "888911112111")
]

for line, expected in cases:
    result = solve_one(line, 12)
    match = "PASS" if result == expected else "FAIL"
    print(f"{match} Input: {line}")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()
