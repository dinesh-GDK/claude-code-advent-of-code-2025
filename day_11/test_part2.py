def parse_input_str(input_str):
    """Parse input string and build a graph adjacency list."""
    graph = {}
    for line in input_str.strip().split('\n'):
        line = line.strip()
        if not line:
            continue

        # Parse line format: "device: output1 output2 ..."
        parts = line.split(':')
        device = parts[0].strip()
        outputs = parts[1].strip().split() if len(parts) > 1 and parts[1].strip() else []
        graph[device] = outputs

    return graph

def count_paths_with_both(graph, start, end, required_nodes, path=None):
    """
    Count all paths from start to end that visit all nodes in required_nodes.
    Uses DFS with path tracking and cycle detection.
    """
    if path is None:
        path = set()

    # Add current node to path
    path = path | {start}

    # Base case: reached the destination
    if start == end:
        # Check if path contains all required nodes
        if all(node in path for node in required_nodes):
            return 1
        else:
            return 0

    # If this device has no outputs, no path exists
    if start not in graph or not graph[start]:
        return 0

    # Recursive case: sum paths through all outputs
    total_paths = 0
    for output in graph[start]:
        # Skip if output is already in current path (cycle detection)
        if output not in path:
            total_paths += count_paths_with_both(graph, output, end, required_nodes, path)

    return total_paths

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

graph = parse_input_str(example)
print("Graph:", graph)

result = count_paths_with_both(graph, 'svr', 'out', {'dac', 'fft'})
print(f"Example result: {result} (expected: 2)")
