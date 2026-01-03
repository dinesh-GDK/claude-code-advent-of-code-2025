import re
from pulp import *

def parse_machine_part2(line):
    """Parse a machine configuration line for Part 2."""
    # Extract button configurations (x,y,z)
    buttons = []
    button_matches = re.findall(r'\(([0-9,]+)\)', line)
    for button_str in button_matches:
        indices = [int(x) for x in button_str.split(',')]
        buttons.append(indices)

    # Extract joltage requirements {a,b,c,...}
    joltage_match = re.search(r'\{([0-9,]+)\}', line)
    joltages = [int(x) for x in joltage_match.group(1).split(',')]

    return joltages, buttons

def find_min_presses_part2(joltages, buttons):
    """Find minimum number of button presses to reach target joltage levels using ILP."""
    num_buttons = len(buttons)
    num_counters = len(joltages)

    # Create the problem
    prob = LpProblem("MinimizeButtonPresses", LpMinimize)

    # Create decision variables (number of times each button is pressed)
    button_vars = [LpVariable(f"button_{i}", lowBound=0, cat='Integer') for i in range(num_buttons)]

    # Objective: minimize total button presses
    prob += lpSum(button_vars)

    # Constraints: each counter must reach its target value
    for counter_idx in range(num_counters):
        # Sum of all button presses that affect this counter
        counter_sum = lpSum([button_vars[button_idx] for button_idx in range(num_buttons)
                            if counter_idx in buttons[button_idx]])
        prob += counter_sum == joltages[counter_idx], f"Counter_{counter_idx}"

    # Solve the problem
    prob.solve(PULP_CBC_CMD(msg=0))

    if prob.status == LpStatusOptimal:
        total_presses = int(value(prob.objective))
        return total_presses
    else:
        return -1

def solve(input_text):
    """Solve the problem."""
    lines = input_text.strip().split('\n')
    total_presses = 0

    for line in lines:
        joltages, buttons = parse_machine_part2(line)
        min_presses = find_min_presses_part2(joltages, buttons)
        total_presses += min_presses

    return total_presses

# Test with example
example = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

example_result = solve(example)
print(f"Example result: {example_result}")
print(f"Expected: 33")

# Read actual input
with open('day_10/input.txt', 'r', encoding='utf-8') as f:
    input_text = f.read()

result = solve(input_text)
print(f"\nPart 2 answer: {result}")
