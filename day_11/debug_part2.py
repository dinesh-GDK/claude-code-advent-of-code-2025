def parse_input(filename):
    """Parse the input file and build a graph adjacency list."""
    graph = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(':')
            device = parts[0].strip()
            outputs = parts[1].strip().split() if len(parts) > 1 and parts[1].strip() else []
            graph[device] = outputs

    return graph

def find_all_paths_with_both(graph, current, end, has_dac, has_fft, path, all_paths):
    """Find all actual paths (for debugging)."""
    # Update flags
    if current == 'dac':
        has_dac = True
    if current == 'fft':
        has_fft = True

    # Add to path
    path = path + [current]

    # Base case
    if current == end:
        if has_dac and has_fft:
            all_paths.append(path)
        return

    # Recursive case
    if current in graph:
        for output in graph[current]:
            if output not in path:  # Avoid cycles
                find_all_paths_with_both(graph, output, end, has_dac, has_fft, path, all_paths)

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

# Write example to file
with open('day_11/example2.txt', 'w') as f:
    f.write(example)

graph = parse_input('day_11/example2.txt')
all_paths = []
find_all_paths_with_both(graph, 'svr', 'out', False, False, [], all_paths)

print(f"Found {len(all_paths)} paths that visit both dac and fft:")
for i, p in enumerate(all_paths, 1):
    print(f"{i}. {' → '.join(p)}")
