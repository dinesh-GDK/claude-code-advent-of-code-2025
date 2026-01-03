# Day 10: Factory

## Part 1 - Indicator Light Configuration

### Problem Understanding
- Each machine has indicator lights (all initially OFF)
- Goal: Configure lights to match target pattern shown in brackets
- Each button toggles specific lights (listed by index)
- Need to find minimum total button presses across all machines

### Key Insights
1. **Binary State System**: Lights are either on (1) or off (0)
2. **Toggle Operation**: Pressing a button flips the state of specified lights
3. **Idempotent Property**: Pressing a button twice = not pressing it at all
4. **XOR Problem**: Each configuration is essentially a XOR of button vectors
5. **Minimization**: Since pressing twice cancels out, we only need to consider pressing each button 0 or 1 times

### Mathematical Model
- Represent each button as a binary vector (1 if it toggles that light, 0 otherwise)
- Target state is also a binary vector
- Problem: Find minimum subset of button vectors that XOR to target

### Strategy
For each machine:
1. Parse the target configuration and button definitions
2. Try all combinations of buttons, starting from smallest number of presses
3. For each combination, simulate button presses (XOR operations)
4. Return the first combination that matches target (this is minimum due to BFS order)

### Algorithm
- Use itertools.combinations to generate button press combinations
- Start with 0 buttons, then 1, then 2, etc.
- For each combination, XOR all button vectors and check if it equals target
- Sum up minimum presses across all machines

## Part 2 - Joltage Counter Configuration

### Problem Understanding
- Now machines need joltage levels configured (ignore indicator lights)
- Each machine has joltage requirements in {curly braces}
- Each requirement has a counter starting at 0
- Buttons now INCREMENT counters by 1 (not toggle)
- Goal: reach exact joltage values with minimum button presses

### Key Insights
1. **Additive System**: Counters accumulate button presses
2. **Linear System**: Each button increments specific counters by 1
3. **Integer Linear Programming**: Need non-negative integer solution
4. **Optimization**: Minimize total button presses while reaching exact targets

### Mathematical Model
- Each button can be pressed 0 or more times
- Pressing button i affects counters listed in button definition
- For each counter, sum of all button effects must equal target value
- Minimize: sum of all button presses

### Strategy
This is an Integer Linear Programming (ILP) problem:
- Variables: xi = number of times to press button i
- Constraints: For each counter j, Σ(aij * xi) = tj where aij=1 if button i affects counter j
- Objective: Minimize Σ(xi)
- Use linear programming solver (scipy or pulp) to find optimal solution
