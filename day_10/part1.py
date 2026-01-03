import re
from itertools import combinations

def parse_machine(line):
    """Parse a machine configuration line."""
    # Extract the indicator pattern [.##.]
    pattern_match = re.search(r'\[(.*?)\]', line)
    pattern = pattern_match.group(1)

    # Convert pattern to binary target (. = 0, # = 1)
    target = [1 if c == '#' else 0 for c in pattern]
    num_lights = len(target)

    # Extract button configurations (x,y,z)
    buttons = []
    button_matches = re.findall(r'\(([0-9,]+)\)', line)
    for button_str in button_matches:
        indices = [int(x) for x in button_str.split(',')]
        # Create binary vector for this button
        button_vector = [0] * num_lights
        for idx in indices:
            button_vector[idx] = 1
        buttons.append(button_vector)

    return target, buttons

def find_min_presses(target, buttons):
    """Find minimum number of button presses to reach target configuration."""
    num_buttons = len(buttons)
    num_lights = len(target)

    # Try increasing number of button presses
    for num_presses in range(num_buttons + 1):
        # Try all combinations of this many buttons
        for button_combo in combinations(range(num_buttons), num_presses):
            # Simulate pressing these buttons
            state = [0] * num_lights
            for button_idx in button_combo:
                # XOR this button's effect
                for i in range(num_lights):
                    state[i] ^= buttons[button_idx][i]

            # Check if we reached target
            if state == target:
                return num_presses

    # Should never reach here if problem is solvable
    return -1

def solve(input_text):
    """Solve the problem."""
    lines = input_text.strip().split('\n')
    total_presses = 0

    for line in lines:
        target, buttons = parse_machine(line)
        min_presses = find_min_presses(target, buttons)
        total_presses += min_presses

    return total_presses

# Test with example
example = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

example_result = solve(example)
print(f"Example result: {example_result}")
print(f"Expected: 7")

# Read actual input
with open('day_10/input.txt', 'r', encoding='utf-8') as f:
    input_text = f.read()

result = solve(input_text)
print(f"\nPart 1 answer: {result}")
