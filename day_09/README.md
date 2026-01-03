# Day 9: Movie Theater

## Part 1

### Problem
Given a list of coordinates representing red tiles on a movie theater floor, find the largest rectangle that can be formed using any two red tiles as opposite corners.

### Strategy
1. Parse the input file to get all red tile coordinates (x, y)
2. For each pair of red tiles, they can serve as opposite corners of a rectangle
3. Calculate the area of each rectangle: area = |x2 - x1| * |y2 - y1|
4. Return the maximum area found

### Example
For the given example with coordinates:
- 7,1
- 11,1
- 11,7
- 9,7
- 9,5
- 2,5
- 2,3
- 7,3

The largest rectangle is between (2,5) and (11,1) with area = |11-2| * |5-1| = 9 * 4 = 36
Wait, let me recalculate: between 2,5 and 11,1: |11-2| = 9, |1-5| = 4, area = 36

Actually from the problem, it says the largest is between 2,5 and 11,1. Let me verify the exact calculation when implementing.

### Implementation Approach
- Read all coordinates into a list
- Use nested loops to check all pairs
- Track maximum area
- Time complexity: O(n^2) where n is the number of red tiles

## Part 2

### Problem Analysis
- Red tiles form a closed polygon (496 tiles)
- Green tiles: edges connecting consecutive red tiles + all tiles inside polygon
- Find largest rectangle with red tile corners where ALL tiles are red or green
- **Challenge**: Bounding box is 96,580 x 96,888 = 9.3 BILLION tiles!
  - Cannot pre-compute all valid tiles
  - Must validate rectangles on-demand with caching

### Previous Attempt Issues
- Attempts with arbitrary area limits (100k, 999k) found wrong answers
- Each limit found a rectangle just below it, suggesting incomplete search
- Need to check all rectangles without artificial area limits
- Use caching and smart pruning instead

### Strategy
1. Build green edge tiles connecting consecutive red tiles
2. For each pair of red tiles as rectangle corners:
   - Calculate area and skip if it can't beat current max
   - For each tile in rectangle, check if valid (with caching):
     - Valid if: red tile, green edge tile, or inside polygon
   - Use point_in_polygon caching to speed up checks
3. Add safety loop breakers (not search space limits):
   - Stop tile validation if rectangle exceeds reasonable size (10M tiles)
   - But continue checking other rectangles
