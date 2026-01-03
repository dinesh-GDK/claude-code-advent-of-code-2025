# Day 11: Reactor

## Part 1: Count All Paths from "you" to "out"

### Problem Understanding
- We have a directed graph of devices with connections
- Each device has outputs that connect to other devices
- Data flows only in one direction (from a device through its outputs)
- We need to find the total number of different paths from the device labeled "you" to the device labeled "out"

### Example Analysis
```
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
```

Paths from "you" to "out":
1. you → bbb → ddd → ggg → out
2. you → bbb → eee → out
3. you → ccc → ddd → ggg → out
4. you → ccc → eee → out
5. you → ccc → fff → out

Total: 5 paths

### Strategy
1. Parse the input to build an adjacency list representation of the graph
2. Use Depth-First Search (DFS) to explore all possible paths from "you" to "out"
3. Count each complete path that reaches "out"
4. Return the total count

### Algorithm
- Build a dictionary/map where each device name maps to a list of its output devices
- Implement recursive DFS:
  - Base case: if current node is "out", count this as 1 path
  - Recursive case: sum the paths from all neighbors of the current node
- Start DFS from "you"

### Complexity
- Time: O(V + E) where V is vertices and E is edges (in worst case we explore all paths)
- Space: O(V) for the recursion stack and graph storage

## Part 2: Count Paths from "svr" to "out" that Visit Both "dac" and "fft"

### Problem Understanding
- Now we need to find paths from "svr" (server rack) to "out"
- But we only count paths that visit BOTH "dac" (digital-to-analog converter) AND "fft" (fast Fourier transform) in any order
- The path must pass through both devices at some point

### Example Analysis
Using the same graph structure, there are many paths from "svr" to "out", but only 2 of them visit both "dac" and "fft".

Example paths that visit both:
- svr → aaa → fft → ccc → eee → dac → fff → ggg → out (visits fft then dac)
- svr → aaa → fft → ccc → ddd → hub → fff → ggg → out (visits fft, and dac is on another branch)

### Strategy
1. Use DFS to enumerate all paths from "svr" to "out"
2. For each complete path, track which devices were visited
3. Count only the paths where both "dac" and "fft" appear in the visited set
4. Return the count

### Algorithm
- Build the graph adjacency list from input
- Implement DFS that tracks the current path:
  - Base case: if we reach "out", check if current path contains both "dac" and "fft"
  - Recursive case: explore all neighbors, adding each to the current path
  - Use backtracking to explore all possible paths
- Start DFS from "svr" with an empty visited set

### Complexity
- Time: O(V + E) for exploring all paths, but may need to track visited nodes per path
- Space: O(V) for recursion stack and path tracking
