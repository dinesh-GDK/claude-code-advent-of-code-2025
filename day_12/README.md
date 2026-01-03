# Day 12: Christmas Tree Farm

## Part 1: Present Packing Problem

**Answer: 460**

### Problem Summary
- Given present shapes (as grids with # and .)
- Given regions (width x height) under trees
- For each region, we have quantities of each present shape that need to fit
- Presents can be rotated and flipped
- # parts can't overlap between presents
- . parts don't block other presents
- Count how many regions can fit all their required presents

### Strategy

This is a 2D bin packing problem with constraints. Approach:

1. **Parse Input**
   - Extract shape definitions (convert to coordinate sets for # positions)
   - Extract region specifications (dimensions + quantities)

2. **Generate Shape Transformations**
   - For each shape, generate all unique rotations (0°, 90°, 180°, 270°)
   - For each rotation, generate flipped version
   - Store as sets of (row, col) coordinates relative to origin

3. **Backtracking Algorithm**
   - For each region, try to place all required presents
   - Use recursive backtracking to try placing each present
   - For each present placement attempt:
     - Try all transformations of the shape
     - Try all positions in the region
     - Check if placement is valid (no # overlap, within bounds)
     - If valid, mark cells as occupied and recurse
     - If all presents placed successfully, return True
     - Otherwise, backtrack and try next position/transformation

4. **Optimization Techniques**
   - Use set operations for fast overlap detection
   - Try placing larger/more constrained shapes first
   - Early termination if clearly impossible (total area check)

5. **Count Valid Regions**
   - For each region, run backtracking
   - Count regions where all presents fit successfully

## Part 2: Completion

**No additional puzzle - automatic completion!**

Part 2 of Day 12 is a narrative completion without an additional puzzle. Upon completing Part 1, both stars are awarded automatically. This is a special "freebie" day in Advent of Code 2025.

The story: After helping the Elves with the present packing problem, more Elves arrive with stars to put atop the Christmas trees. A large Christmas tree magically gets its star, and you go look for a ladder - only 23 stars to go!
