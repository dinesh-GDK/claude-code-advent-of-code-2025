# Day 4: Printing Department

## Part 1: Finding Accessible Paper Rolls

### Problem Summary
We need to find which rolls of paper (@) can be accessed by forklifts. A roll can be accessed if it has **fewer than 4** rolls of paper in its 8 adjacent positions (N, NE, E, SE, S, SW, W, NW).

### Strategy
1. Parse the input grid to identify all positions
2. For each cell containing '@':
   - Count the number of '@' symbols in all 8 adjacent cells
   - An adjacent position is valid if it's within grid bounds
3. If the count of adjacent '@' is less than 4, mark it as accessible
4. Return the total count of accessible rolls

### Example Analysis
From the example grid:
```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

13 rolls are accessible (those with < 4 adjacent '@' symbols).

## Part 2: Iterative Removal of Paper Rolls

### Problem Summary
Now we need to find the total number of rolls that can be removed by repeating the removal process. Once accessible rolls are removed, new rolls may become accessible.

### Strategy
1. Start with the original grid
2. Find all accessible rolls (< 4 adjacent '@' symbols)
3. Remove all accessible rolls (replace '@' with '.')
4. Repeat steps 2-3 until no more rolls can be removed
5. Count and return the total number of rolls removed across all iterations

### Example Analysis
From the same example grid:
- Iteration 1: Remove 13 rolls
- Iteration 2: Remove 12 rolls
- Iteration 3: Remove 7 rolls
- Iteration 4: Remove 5 rolls
- Iteration 5: Remove 2 rolls
- Iterations 6-9: Remove 1 roll each
- **Total: 43 rolls removed**

### Implementation Notes
- Use a loop to repeatedly find and remove accessible rolls
- Stop when no accessible rolls are found in an iteration
- Keep track of total rolls removed
