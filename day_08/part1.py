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

def solve(filename):
    # Parse input
    boxes = []
    with open(filename, encoding='utf-8-sig') as f:
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

    # Attempt the 1000 closest pairs
    uf = UnionFind(n)
    successful = 0
    for attempt in range(1000):
        dist, i, j = distances[attempt]
        if uf.union(i, j):
            successful += 1

    print(f"Made {successful} successful connections out of 1000 attempts")

    # Count circuit sizes
    circuit_sizes = defaultdict(int)
    for i in range(n):
        root = uf.find(i)
        circuit_sizes[root] += 1

    # Get the three largest circuits
    sizes = sorted(circuit_sizes.values(), reverse=True)
    print(f"Circuit sizes: {sizes}")
    print(f"Three largest: {sizes[0]}, {sizes[1]}, {sizes[2]}")

    result = sizes[0] * sizes[1] * sizes[2]
    return result

if __name__ == "__main__":
    # Test with example if provided
    result = solve("day_08/input.txt")
    print(f"\nAnswer: {result}")
