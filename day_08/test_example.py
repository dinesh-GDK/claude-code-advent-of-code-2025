import math
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def solve(filename, num_connections):
    # Parse input
    boxes = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                coords = list(map(int, line.split(',')))
                boxes.append(tuple(coords))

    n = len(boxes)
    print(f"Number of boxes: {n}")

    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = boxes[i]
            x2, y2, z2 = boxes[j]
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            distances.append((dist, i, j))

    # Sort by distance
    distances.sort()

    # Show first few distances
    print("\nFirst 10 shortest distances:")
    for i in range(min(10, len(distances))):
        dist, idx1, idx2 = distances[i]
        print(f"  {i+1}. Boxes {idx1} and {idx2}: distance = {dist:.2f}")

    # Connect the closest pairs
    uf = UnionFind(n)
    connections = 0
    for dist, i, j in distances:
        if connections >= num_connections:
            break
        if uf.union(i, j):
            connections += 1

    print(f"\nMade {connections} connections")

    # Count circuit sizes
    circuit_sizes = defaultdict(int)
    for i in range(n):
        root = uf.find(i)
        circuit_sizes[root] += 1

    # Get the three largest circuits
    sizes = sorted(circuit_sizes.values(), reverse=True)
    print(f"All circuit sizes: {sizes}")
    print(f"Three largest: {sizes[0]}, {sizes[1]}, {sizes[2]}")

    result = sizes[0] * sizes[1] * sizes[2]
    return result

if __name__ == "__main__":
    # Test with example (10 connections for 20 boxes)
    result = solve("day_08/example.txt", 10)
    print(f"\nAnswer: {result}")
    print(f"Expected: 40")
