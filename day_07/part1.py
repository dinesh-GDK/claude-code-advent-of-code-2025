from collections import deque

def solve(grid):
    """
    Simulate tachyon beam splitting through the manifold.

    Rules:
    - Beams start at 'S' and move downward
    - Beams pass through '.' (empty space)
    - When a beam hits '^' (splitter), it stops and creates two new beams
      at the immediate left and right positions
    - Count total number of splits
    """
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    # Find starting position 'S'
    start_r, start_c = None, None
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 'S':
                start_r, start_c = r, c
                break
        if start_r is not None:
            break

    # BFS simulation
    queue = deque([(start_r, start_c)])
    visited = set()
    splits = 0

    while queue:
        r, c = queue.popleft()

        # Skip if out of bounds
        if r < 0 or r >= height or c < 0 or c >= width:
            continue

        # Skip if already visited this position
        if (r, c) in visited:
            continue

        visited.add((r, c))

        # Check current position
        if grid[r][c] == '^':
            # Hit a splitter! Count this split
            splits += 1
            # Create two new beams at left and right positions
            queue.append((r, c - 1))
            queue.append((r, c + 1))
        elif grid[r][c] in ['.', 'S']:
            # Empty space or starting position - continue downward
            queue.append((r + 1, c))

    return splits

def main():
    # Read input
    with open('day_07/input.txt', 'r', encoding='utf-8-sig') as f:
        lines = [line.rstrip('\n\r') for line in f if line.strip()]

    # Solve
    result = solve(lines)
    print(f"Total beam splits: {result}")

if __name__ == "__main__":
    main()
