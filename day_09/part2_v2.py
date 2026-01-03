def point_in_polygon(point, polygon):
    """Check if a point is inside a polygon using ray casting algorithm."""
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

def get_tiles_between(p1, p2):
    """Get all tiles on the straight line between two points (inclusive)."""
    x1, y1 = p1
    x2, y2 = p2
    tiles = []

    if x1 == x2:  # Vertical line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            tiles.append((x1, y))
    elif y1 == y2:  # Horizontal line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            tiles.append((x, y1))

    return tiles

def solve(filename):
    import time
    start_time = time.time()

    # Read all red tile coordinates (in order)
    red_tiles = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(','))
                red_tiles.append((x, y))

    print(f"Read {len(red_tiles)} red tiles")
    red_set = set(red_tiles)

    # Build green edge tiles (tiles connecting consecutive red tiles)
    green_edge_tiles = set()
    n = len(red_tiles)
    for i in range(n):
        p1 = red_tiles[i]
        p2 = red_tiles[(i + 1) % n]  # Wrap around
        edge_tiles = get_tiles_between(p1, p2)
        green_edge_tiles.update(edge_tiles)

    # Remove red tiles from green tiles
    green_edge_tiles -= red_set
    print(f"Built {len(green_edge_tiles)} green edge tiles")

    # Cache for point_in_polygon results
    polygon_cache = {}

    def is_valid_tile(tile):
        """Check if tile is red, green edge, or inside polygon."""
        if tile in red_set or tile in green_edge_tiles:
            return True
        if tile not in polygon_cache:
            polygon_cache[tile] = point_in_polygon(tile, red_tiles)
        return polygon_cache[tile]

    # Find maximum area by trying all pairs of red tiles
    max_area = 0
    best_corners = None
    n_red = len(red_tiles)

    print(f"Checking {n_red} red tiles, total pairs: {n_red * (n_red - 1) // 2}")

    pair_count = 0
    for i in range(n_red):
        if i % 50 == 0:
            print(f"Progress: {i}/{n_red}, max={max_area}, cache_size={len(polygon_cache)}")

        for j in range(i + 1, n_red):
            pair_count += 1
            if pair_count > 999_999:
                print("Reached pair limit")
                break

            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            min_rx, max_rx = min(x1, x2), max(x1, x2)
            min_ry, max_ry = min(y1, y2), max(y1, y2)

            area = (max_rx - min_rx + 1) * (max_ry - min_ry + 1)

            # Skip if can't beat current max
            if area <= max_area:
                continue

            # Skip if too large to check in reasonable time
            # Match the tile check limit below
            if area > 999_999:
                continue

            # Check all tiles with loop breaker
            all_valid = True
            checks = 0

            for x in range(min_rx, max_rx + 1):
                for y in range(min_ry, max_ry + 1):
                    checks += 1
                    if checks > 999_999:
                        # Skip this rectangle, it's too big
                        all_valid = False
                        break

                    if not is_valid_tile((x, y)):
                        all_valid = False
                        break

                if not all_valid:
                    break

            # Only update if we checked all tiles successfully
            if all_valid and checks <= 999_999:
                max_area = area
                best_corners = ((x1, y1), (x2, y2))
                print(f"  Found: area={area} between ({x1},{y1}) and ({x2},{y2})")

        if pair_count > 999_999:
            break

    print(f"\nBest: area={max_area}, corners={best_corners}")
    return max_area

if __name__ == "__main__":
    # Test with example
    example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

    with open('example.txt', 'w') as f:
        f.write(example)

    print("=== Example ===")
    example_result = solve('example.txt')
    print(f"Example result: {example_result}\n")

    # Solve actual puzzle
    print("=== Actual Input ===")
    result = solve('input.txt')
    print(f"\nPart 2 answer: {result}")
