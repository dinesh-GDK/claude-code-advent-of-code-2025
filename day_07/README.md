# Day 7: Laboratories

## Part 1

### Problem Understanding
- We have a tachyon manifold represented as a grid
- A tachyon beam starts at position 'S' and moves **downward**
- The beam passes through empty space ('.')
- When a beam encounters a splitter ('^'):
  - The current beam stops
  - Two new beams are created from the positions immediately to the LEFT and RIGHT of the splitter
  - These new beams also move downward
- We need to count the total number of times beams are split

### Strategy
1. Parse the input grid to find the starting position 'S' and all splitter positions
2. Use BFS/simulation to track beam positions:
   - Start with one beam at the 'S' position
   - For each beam, simulate it moving downward row by row
   - When a beam encounters a '^' splitter:
     - Increment the split counter
     - Create two new beams at (row, col-1) and (row, col+1)
     - These new beams continue moving downward from their starting positions
3. Track which (row, col) positions have been visited by beams to handle:
   - Multiple beams converging at the same position
   - Counting splits correctly (each beam hitting a splitter counts as a split)
4. Continue simulation until all beams exit the grid (row >= height)

### Key Insights
- Each time ANY beam hits a splitter, it's counted as one split
- Multiple beams can occupy the same position
- We need to track beam states carefully to count all split events
- The problem is essentially simulating beam propagation through the manifold

### Example
In the given example, the beam is split 21 times total as it propagates through the manifold structure.

### Answer: 1628

## Part 2

### Problem Understanding
- The manifold is actually a **quantum tachyon manifold**
- Only a **single tachyon particle** is sent through the manifold
- The particle takes **both the left and right path** at each splitter encountered
- Uses the **many-worlds interpretation**: when a particle reaches a splitter, **time itself splits**
  - In one timeline, the particle went left
  - In the other timeline, the particle went right
- We need to count the **total number of different timelines** that exist after the single particle completes all possible journeys through the manifold

### Strategy
1. Use recursion with memoization to count all possible paths (timelines) through the manifold
2. For each position (r, c):
   - If out of bounds: return 1 (this is one timeline that exited)
   - If at a splitter ('^'): return count_paths(r, c-1) + count_paths(r, c+1)
   - If at empty space ('.' or 'S'): return count_paths(r+1, c)
3. Start from the 'S' position and count all possible paths

### Key Insights
- Unlike Part 1, we DON'T merge beams at the same position
- Each unique path through the manifold represents a distinct timeline
- Even if two paths end at the same position, they are different timelines if they took different routes
- The answer is the sum of all paths that exit the manifold
- This is a tree-counting problem where each splitter creates a branch point

### Example
In the given example, the particle ends up on 40 different timelines.
