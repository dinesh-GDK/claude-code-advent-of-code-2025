# Day 8: Playground

## Part 1

### Problem Summary
- We have junction boxes positioned in 3D space (x, y, z coordinates)
- Need to connect the 1000 pairs of junction boxes that are closest together
- When two boxes are connected, they become part of the same circuit
- After making 1000 connections, find the product of the sizes of the three largest circuits

### Strategy

1. **Parse Input**: Read junction box coordinates from input file
2. **Calculate Distances**: For all pairs of junction boxes, calculate Euclidean distance: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
3. **Sort by Distance**: Sort all pairs by their distance
4. **Union-Find Structure**: Use a Union-Find (Disjoint Set Union) data structure to track circuits
5. **Make Connections**: Connect the 1000 closest pairs of boxes, merging their circuits
6. **Count Circuit Sizes**: After all connections, count how many boxes are in each circuit
7. **Find Answer**: Multiply the sizes of the three largest circuits

### Key Insights
- Union-Find is perfect for this problem as it efficiently tracks connected components
- We don't need to store actual connections, just track which boxes belong to which circuit
- After 1000 connections with N boxes, we'll have N-1000 circuits (assuming no duplicate connections)

### Example
With 20 boxes and 10 connections:
- Result: 5 × 4 × 2 = 40

### Answer
Part 1: **105952**

## Part 2

### Problem Summary
- Continue connecting junction boxes until they're all in one large circuit
- Connect pairs in order of increasing distance (closest first)
- Find the last pair that needs to be connected to form one complete circuit
- Return the product of the X coordinates of those two junction boxes

### Strategy

1. **Reuse Part 1 Setup**: Parse input, calculate distances, sort pairs
2. **Connect Until One Circuit**: Continue connecting pairs until all boxes are in the same circuit
3. **Track Last Connection**: Keep track of which pair was connected last
4. **Check Circuit Count**: After each connection, check if all boxes are in one circuit (only 1 root in Union-Find)
5. **Return Product**: When complete, return X1 × X2 of the last connected pair

### Key Insights
- With N boxes, we need exactly N-1 connections to form one circuit
- We can check if all boxes are in one circuit by counting unique roots in Union-Find
- The last connection is what we're looking for

### Example
With 20 boxes:
- Continue connecting beyond the first 10
- The connection between boxes at 216,146,977 and 117,168,530 completes the circuit
- Result: 216 × 117 = 25272

### Answer
Part 2: **975931446**
