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

def count_paths_with_both(graph, current, end, required_nodes, visited_required, visited_in_path, memo):
    """
    Count all paths from current to end that visit all nodes in required_nodes.
    Uses DFS with memoization on (node, visited_required_tuple, visited_in_path_tuple).
    """
    # Create a memoization key
    # We need to track which nodes in path to avoid cycles
    memo_key = (current, frozenset(visited_required), frozenset(visited_in_path))

    if memo_key in memo:
        return memo[memo_key]

    # Base case: reached the destination
    if current == end:
        # Check if we've visited all required nodes
        if len(visited_required) == len(required_nodes):
            return 1
        else:
            return 0

    # If this device has no outputs, no path exists
    if current not in graph or not graph[current]:
        return 0

    # Recursive case: sum paths through all outputs
    total_paths = 0
    for output in graph[current]:
        # Skip if output is already in current path (cycle detection)
        if output in visited_in_path:
            continue

        # Update visited_required if output is a required node
        new_visited_required = visited_required.copy()
        if output in required_nodes:
            new_visited_required.add(output)

        # Update path with current output
        new_visited_in_path = visited_in_path | {output}

        total_paths += count_paths_with_both(
            graph, output, end, required_nodes,
            new_visited_required, new_visited_in_path, memo
        )

    memo[memo_key] = total_paths
    return total_paths

def solve(filename):
    """Solve part 2: count paths from 'svr' to 'out' that visit both 'dac' and 'fft'."""
    graph = parse_input(filename)
    required_nodes = {'dac', 'fft'}

    # Track which required nodes we've visited and current path
    visited_required = set()
    if 'svr' in required_nodes:
        visited_required.add('svr')

    visited_in_path = {'svr'}
    memo = {}

    result = count_paths_with_both(graph, 'svr', 'out', required_nodes, visited_required, visited_in_path, memo)
    return result

if __name__ == '__main__':
    # Test with example
    example = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

    # Write example to temporary file
    with open('day_11/example2.txt', 'w') as f:
        f.write(example)

    # Test with example (should be 2)
    example_result = solve('day_11/example2.txt')
    print(f"Example result: {example_result} (expected: 2)")

    # Solve with actual input
    result = solve('day_11/input.txt')
    print(f"Part 2 answer: {result}")
