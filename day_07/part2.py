from functools import lru_cache

def solve(grid):
    """
    Count the number of different timelines in a quantum tachyon manifold.

    In the quantum version:
    - A single particle is sent through
    - At each splitter, the timeline splits (particle takes both paths)
    - We count the total number of distinct timelines (paths) that exit the manifold
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

    @lru_cache(maxsize=None)
    def count_paths(r, c):
        """
        Count the number of timelines (paths) starting from position (r, c).

        Returns:
            Number of distinct paths that exit the manifold from this position
        """
        # Out of bounds - this is one timeline that exited the manifold
        if r < 0 or r >= height or c < 0 or c >= width:
            return 1

        # Check current position
        if grid[r][c] == '^':
            # Hit a splitter! Timeline splits into two
            # Count paths from both left and right positions
            left_timelines = count_paths(r, c - 1)
            right_timelines = count_paths(r, c + 1)
            return left_timelines + right_timelines
        else:  # '.' or 'S'
            # Empty space or starting position - continue downward
            return count_paths(r + 1, c)

    return count_paths(start_r, start_c)

def main():
    # Read input
    with open('day_07/input.txt', 'r', encoding='utf-8-sig') as f:
        lines = [line.rstrip('\n\r') for line in f if line.strip()]

    # Solve
    result = solve(lines)
    print(f"Total timelines: {result}")

if __name__ == "__main__":
    main()
