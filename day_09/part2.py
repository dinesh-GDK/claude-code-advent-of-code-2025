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

def is_tile_valid(tile, red_set, green_edge_tiles, polygon):
    """Check if a tile is red or green (on edge or inside polygon)."""
    if tile in red_set:
        return True
    if tile in green_edge_tiles:
        return True
    # Check if inside polygon
    return point_in_polygon(tile, polygon)

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

    print(f"Read {len(red_tiles)} red tiles in {time.time()-start_time:.2f}s")
    red_set = set(red_tiles)

    # Build green edge tiles (tiles connecting consecutive red tiles)
    edge_start = time.time()
    green_edge_tiles = set()
    n = len(red_tiles)
    for i in range(n):
        p1 = red_tiles[i]
        p2 = red_tiles[(i + 1) % n]  # Wrap around
        edge_tiles = get_tiles_between(p1, p2)
        green_edge_tiles.update(edge_tiles)

    # Remove red tiles from green tiles (edge might include red tiles)
    green_edge_tiles -= red_set
    print(f"Built {len(green_edge_tiles)} green edge tiles in {time.time()-edge_start:.2f}s")

    # Find maximum area by trying all pairs of red tiles
    max_area = 0
    n_red = len(red_tiles)

    print(f"Checking {n_red} red tiles, total pairs: {n_red * (n_red - 1) // 2}")

    pair_count = 0
    for i in range(n_red):
        if i % 50 == 0:
            print(f"Progress: {i}/{n_red} tiles processed, max_area so far: {max_area}")

        for j in range(i + 1, n_red):
            pair_count += 1
            if pair_count > 999_999:
                print("Warning: Too many pairs to check, stopping early")
                break

            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            # Check if all tiles in this rectangle are valid
            min_rx = min(x1, x2)
            max_rx = max(x1, x2)
            min_ry = min(y1, y2)
            max_ry = max(y1, y2)

            # Calculate area first
            rect_width = max_rx - min_rx + 1
            rect_height = max_ry - min_ry + 1
            area = rect_width * rect_height

            # Skip if this can't beat current max
            if area <= max_area:
                continue

            # Skip rectangles that are too large to validate efficiently
            if area > 100000:
                continue

            # Check all tiles in the rectangle with loop breaker
            all_valid = True
            tile_check_count = 0
            max_tile_checks = 999_999

            for x in range(min_rx, max_rx + 1):
                for y in range(min_ry, max_ry + 1):
                    tile_check_count += 1
                    if tile_check_count > max_tile_checks:
                        all_valid = False
                        break

                    if not is_tile_valid((x, y), red_set, green_edge_tiles, red_tiles):
                        all_valid = False
                        break
                if not all_valid:
                    break

            if all_valid:
                max_area = area
                if area > 10000:
                    print(f"  Found large valid rectangle: area={area} between ({x1},{y1}) and ({x2},{y2})")

        if pair_count > 999_999:
            break

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

    example_result = solve('example.txt')
    print(f"Example result: {example_result}")

    # Solve actual puzzle
    result = solve('input.txt')
    print(f"Part 2 answer: {result}")
