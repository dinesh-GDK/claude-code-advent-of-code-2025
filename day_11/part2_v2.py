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

def count_paths_with_both(graph, current, end, has_dac, has_fft, memo):
    """
    Count paths from current to end that have visited dac and fft.
    State: (current_node, has_visited_dac, has_visited_fft)
    This assumes the graph is acyclic (DAG).
    """
    # Memoization key
    key = (current, has_dac, has_fft)
    if key in memo:
        return memo[key]

    # Update flags if current node is dac or fft
    if current == 'dac':
        has_dac = True
    if current == 'fft':
        has_fft = True

    # Base case: reached the destination
    if current == end:
        # Count this path only if we've visited both dac and fft
        result = 1 if (has_dac and has_fft) else 0
        memo[key] = result
        return result

    # If this device has no outputs, no path exists
    if current not in graph or not graph[current]:
        memo[key] = 0
        return 0

    # Recursive case: sum paths through all outputs
    total_paths = 0
    for output in graph[current]:
        total_paths += count_paths_with_both(graph, output, end, has_dac, has_fft, memo)

    memo[key] = total_paths
    return total_paths

def solve(filename):
    """Solve part 2: count paths from 'svr' to 'out' that visit both 'dac' and 'fft'."""
    graph = parse_input(filename)
    memo = {}

    # Start from 'svr', initially haven't visited dac or fft
    has_dac = ('svr' == 'dac')
    has_fft = ('svr' == 'fft')

    result = count_paths_with_both(graph, 'svr', 'out', has_dac, has_fft, memo)
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
