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

    # Precompute all valid tiles within bounding box
    print("Precomputing valid tiles...")
    precompute_start = time.time()

    min_x = min(x for x, y in red_tiles)
    max_x = max(x for x, y in red_tiles)
    min_y = min(y for x, y in red_tiles)
    max_y = max(y for x, y in red_tiles)

    print(f"Bounding box: ({min_x},{min_y}) to ({max_x},{max_y})")

    valid_tiles = red_set | green_edge_tiles

    # Sample points to check if we should precompute all tiles
    # For huge bounding boxes, we'll use on-demand checking instead
    bbox_area = (max_x - min_x + 1) * (max_y - min_y + 1)
    print(f"Bounding box area: {bbox_area}")

    if bbox_area < 10_000_000:  # Only precompute if reasonable size
        print("Precomputing all valid tiles inside polygon...")
        tiles_checked = 0
        for x in range(min_x, max_x + 1):
            if x % 10000 == 0:
                print(f"  Checking x={x}/{max_x}")
            for y in range(min_y, max_y + 1):
                tiles_checked += 1
                if tiles_checked > 10_000_000:  # Safety limit
                    print("Too many tiles to precompute, will check on-demand")
                    break
                if (x, y) not in valid_tiles and point_in_polygon((x, y), red_tiles):
                    valid_tiles.add((x, y))
            if tiles_checked > 10_000_000:
                break
        print(f"Precomputed {len(valid_tiles)} valid tiles in {time.time()-precompute_start:.2f}s")
    else:
        print("Bounding box too large, will check tiles on-demand")

    # Find maximum area by trying all pairs of red tiles
    max_area = 0
    n_red = len(red_tiles)
    best_corners = None

    print(f"Checking {n_red} red tiles, total pairs: {n_red * (n_red - 1) // 2}")

    pair_count = 0
    for i in range(n_red):
        if i % 50 == 0:
            print(f"Progress: {i}/{n_red} tiles processed, max_area so far: {max_area}")

        for j in range(i + 1, n_red):
            pair_count += 1
            if pair_count > 999_999:
                print("Warning: Checked 999,999 pairs, stopping")
                break

            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            # Calculate rectangle bounds
            min_rx = min(x1, x2)
            max_rx = max(x1, x2)
            min_ry = min(y1, y2)
            max_ry = max(y1, y2)

            # Calculate area
            rect_width = max_rx - min_rx + 1
            rect_height = max_ry - min_ry + 1
            area = rect_width * rect_height

            # Skip if this can't beat current max
            if area <= max_area:
                continue

            # Check all tiles in the rectangle (with loop breaker)
            all_valid = True
            tile_check_count = 0
            max_tile_checks = 500_000  # Increased limit

            for x in range(min_rx, max_rx + 1):
                for y in range(min_ry, max_ry + 1):
                    tile_check_count += 1
                    if tile_check_count > max_tile_checks:
                        # Skip this rectangle if it's too large to check
                        all_valid = False
                        break

                    # Check if tile is valid (in precomputed set or check on-demand)
                    tile = (x, y)
                    if tile not in valid_tiles:
                        # If not precomputed, check on-demand
                        if not point_in_polygon(tile, red_tiles):
                            all_valid = False
                            break

                if not all_valid:
                    break

            if all_valid and tile_check_count <= max_tile_checks:
                max_area = area
                best_corners = ((x1, y1), (x2, y2))
                print(f"  Found valid rectangle: area={area} between ({x1},{y1}) and ({x2},{y2})")

        if pair_count > 999_999:
            break

    print(f"\nBest rectangle: area={max_area} between {best_corners}")
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
    print()

    # Solve actual puzzle
    result = solve('input.txt')
    print(f"Part 2 answer: {result}")
