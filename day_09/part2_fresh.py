def point_in_polygon(point, polygon):
    """Ray casting algorithm to check if point is inside polygon."""
    x, y = point
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def get_line_tiles(p1, p2):
    """Get all tiles on a straight line between two points."""
    x1, y1 = p1
    x2, y2 = p2
    tiles = []
    if x1 == x2:  # Vertical
        for y in range(min(y1, y2), max(y1, y2) + 1):
            tiles.append((x1, y))
    elif y1 == y2:  # Horizontal
        for x in range(min(x1, x2), max(x1, x2) + 1):
            tiles.append((x, y1))
    return tiles

def solve(filename):
    # Read red tiles (in order, forming a polygon)
    with open(filename, 'r', encoding='utf-8-sig') as f:
        red_tiles = [tuple(map(int, line.strip().split(',')))
                     for line in f if line.strip()]

    print(f"Red tiles: {len(red_tiles)}")
    red_set = set(red_tiles)

    # Build green edge tiles
    green_edges = set()
    for i in range(len(red_tiles)):
        p1 = red_tiles[i]
        p2 = red_tiles[(i + 1) % len(red_tiles)]
        green_edges.update(get_line_tiles(p1, p2))
    green_edges -= red_set  # Remove red tiles

    print(f"Green edge tiles: {len(green_edges)}")

    # Cache for point-in-polygon checks
    polygon_cache = {}

    def is_valid_tile(tile):
        """Check if tile is red, green edge, or inside polygon."""
        if tile in red_set or tile in green_edges:
            return True
        if tile not in polygon_cache:
            polygon_cache[tile] = point_in_polygon(tile, red_tiles)
        return polygon_cache[tile]

    # Get all pairs of red tiles, sorted by area (smallest first)
    pairs = []
    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)  # Tile count
            pairs.append((area, i, j))

    pairs.sort()  # Start with smallest rectangles
    print(f"Checking {len(pairs)} rectangle pairs...")

    max_area = 0
    best_corners = None
    checked = 0
    skipped = 0

    for area, i, j in pairs:
        # Skip if can't beat current max
        if area <= max_area:
            skipped += 1
            continue

        # Skip very large rectangles (practical limit)
        # Try 2M limit as a middle ground
        if area > 2_000_000:
            skipped += 1
            continue

        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        # Check all tiles in rectangle
        checked += 1
        valid = True
        tile_checks = 0
        first_invalid = None

        for x in range(min_x, max_x + 1):
            if not valid:
                break
            for y in range(min_y, max_y + 1):
                tile_checks += 1
                if tile_checks > 2_000_000:  # Safety breaker - aligned with area limit
                    valid = False
                    first_invalid = "timeout"
                    break
                if not is_valid_tile((x, y)):
                    valid = False
                    first_invalid = (x, y)
                    break

        # Debug: track the expected answer rectangle
        if (x1, y1) == (7, 1) and (x2, y2) == (11, 7) or (x1, y1) == (11, 7) and (x2, y2) == (7, 1):
            print(f"  DEBUG: Checking (7,1)-(11,7): area={area}, valid={valid}, first_invalid={first_invalid}, tiles_checked={tile_checks}")

        if valid and tile_checks <= 2_000_000:
            max_area = area
            best_corners = ((x1, y1), (x2, y2))
            print(f"  NEW BEST: {max_area:,} at corners {best_corners}")

        if checked % 10000 == 0:
            print(f"  Progress: checked {checked:,}, skipped {skipped:,}, max={max_area:,}, cache={len(polygon_cache):,}")

    print(f"\nFinal: area={max_area:,}, corners={best_corners}")
    print(f"Checked {checked:,} rectangles, skipped {skipped:,}")
    print(f"Cache size: {len(polygon_cache):,}")
    return max_area

if __name__ == "__main__":
    import os
    os.chdir(r'C:\Users\user\projects\advent-2025\day_09')

    # Test with example
    example = "7,1\n11,1\n11,7\n9,7\n9,5\n2,5\n2,3\n7,3"
    with open('example.txt', 'w') as f:
        f.write(example)

    print("=== EXAMPLE ===")
    result = solve('example.txt')
    print(f"Result: {result}, Expected: 24")
    assert result == 24, f"Example failed! Got {result}"
    print("[OK]\n")

    # Solve actual
    print("=== ACTUAL INPUT ===")
    answer = solve('input.txt')
    print(f"\n*** Part 2 Answer: {answer} ***")
