def find_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Directions for 8 adjacent cells: N, NE, E, SE, S, SW, W, NW
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    accessible = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                # Count adjacent '@' symbols
                adjacent_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            adjacent_count += 1

                # A roll is accessible if it has fewer than 4 adjacent rolls
                if adjacent_count < 4:
                    accessible.append((r, c))

    return accessible

def remove_rolls_iteratively(grid):
    total_removed = 0

    while True:
        # Find all accessible rolls
        accessible = find_accessible_rolls(grid)

        if not accessible:
            # No more accessible rolls, stop
            break

        # Remove all accessible rolls
        for r, c in accessible:
            grid[r][c] = '.'

        # Count removed in this iteration
        removed_count = len(accessible)
        total_removed += removed_count

    return total_removed

def main():
    with open('day_04/input.txt', 'r', encoding='utf-8-sig') as f:
        lines = f.read().strip().split('\n')

    grid = [list(line) for line in lines]
    result = remove_rolls_iteratively(grid)
    print(f"Total rolls removed: {result}")
    return result

if __name__ == "__main__":
    main()
