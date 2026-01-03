def parse_input(filename):
    """Parse the input file and build a graph adjacency list."""
    graph = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Parse line format: "device: output1 output2 ..."
            parts = line.split(':')
            device = parts[0].strip()
            outputs = parts[1].strip().split() if len(parts) > 1 and parts[1].strip() else []
            graph[device] = outputs

    return graph

def count_paths(graph, start, end, memo=None):
    """Count all paths from start to end using DFS with memoization."""
    if memo is None:
        memo = {}

    # If we've already computed paths from this node, return cached result
    if start in memo:
        return memo[start]

    # Base case: reached the destination
    if start == end:
        return 1

    # If this device has no outputs, no path exists
    if start not in graph or not graph[start]:
        return 0

    # Recursive case: sum paths through all outputs
    total_paths = 0
    for output in graph[start]:
        total_paths += count_paths(graph, output, end, memo)

    # Cache the result
    memo[start] = total_paths
    return total_paths

def solve(filename):
    """Solve part 1: count paths from 'you' to 'out'."""
    graph = parse_input(filename)
    result = count_paths(graph, 'you', 'out')
    return result

if __name__ == '__main__':
    # Test with example
    example = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

    # Write example to temporary file
    with open('day_11/example.txt', 'w') as f:
        f.write(example)

    # Test with example (should be 5)
    example_result = solve('day_11/example.txt')
    print(f"Example result: {example_result} (expected: 5)")

    # Solve with actual input
    result = solve('day_11/input.txt')
    print(f"Part 1 answer: {result}")
