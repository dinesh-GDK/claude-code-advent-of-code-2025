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

    def count_circuits(self):
        """Count the number of distinct circuits"""
        roots = set()
        for i in range(len(self.parent)):
            roots.add(self.find(i))
        return len(roots)

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

    # Connect pairs until all boxes are in one circuit
    uf = UnionFind(n)
    last_i, last_j = None, None

    for dist, i, j in distances:
        if uf.union(i, j):
            last_i, last_j = i, j
            circuits = uf.count_circuits()

            # Check if we're down to one circuit
            if circuits == 1:
                print(f"All boxes connected in one circuit!")
                print(f"Last connection: boxes {i} and {j}")
                print(f"  Box {i}: {boxes[i]}")
                print(f"  Box {j}: {boxes[j]}")
                break

    # Calculate result
    x1 = boxes[last_i][0]
    x2 = boxes[last_j][0]
    result = x1 * x2

    print(f"\nX coordinates: {x1} and {x2}")
    print(f"Product: {x1} × {x2} = {result}")

    return result

if __name__ == "__main__":
    result = solve("day_08/input.txt")
    print(f"\nAnswer: {result}")
