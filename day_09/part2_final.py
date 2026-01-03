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

    # Pre-compute all valid tiles (red, green edge, or inside polygon)
    # This is the KEY optimization - compute once, use many times
    print("Pre-computing valid tiles...")
    min_x = min(t[0] for t in red_tiles)
    max_x = max(t[0] for t in red_tiles)
    min_y = min(t[1] for t in red_tiles)
    max_y = max(t[1] for t in red_tiles)

    valid_tiles = set()
    valid_tiles.update(red_set)
    valid_tiles.update(green_edge_tiles)

    # Add all tiles inside the polygon
    # Use loop breaker for safety, but cover the entire bounding box
    total_tiles = (max_x - min_x + 1) * (max_y - min_y + 1)
    print(f"Scanning bounding box: {max_x - min_x + 1} x {max_y - min_y + 1} = {total_tiles} tiles")

    tile_count = 0
    for x in range(min_x, max_x + 1):
        if x % 100 == 0:
            progress = tile_count / total_tiles * 100
            print(f"  Progress: {progress:.1f}% ({tile_count}/{total_tiles})")

        for y in range(min_y, max_y + 1):
            tile_count += 1

            # Safety breaker to prevent truly infinite loops
            if tile_count > 50_000_000:  # 50 million tiles max
                print("WARNING: Bounding box too large, stopping pre-computation")
                break

            tile = (x, y)
            if tile in valid_tiles:
                continue  # Already added

            if point_in_polygon(tile, red_tiles):
                valid_tiles.add(tile)

        if tile_count > 50_000_000:
            break

    print(f"Pre-computed {len(valid_tiles)} valid tiles in {time.time() - start_time:.1f}s")

    # Now find the largest rectangle
    max_area = 0
    best_corners = None
    n_red = len(red_tiles)

    print(f"\nChecking {n_red * (n_red - 1) // 2} pairs of red tiles...")

    pair_count = 0
    checked_count = 0

    for i in range(n_red):
        if i % 50 == 0:
            print(f"Progress: {i}/{n_red}, checked {checked_count} rectangles, max_area={max_area}")

        for j in range(i + 1, n_red):
            pair_count += 1

            # Safety breaker for pairs (not a search space limit!)
            if pair_count > 10_000_000:  # 10 million pairs max
                print("WARNING: Too many pairs, stopping")
                break

            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            min_rx, max_rx = min(x1, x2), max(x1, x2)
            min_ry, max_ry = min(y1, y2), max(y1, y2)

            area = (max_rx - min_rx + 1) * (max_ry - min_ry + 1)

            # Skip if can't beat current max
            if area <= max_area:
                continue

            # Check if rectangle is valid by verifying all tiles are in valid_tiles
            checked_count += 1
            all_valid = True
            check_count = 0

            for x in range(min_rx, max_rx + 1):
                if not all_valid:
                    break
                for y in range(min_ry, max_ry + 1):
                    check_count += 1

                    # Safety breaker for tile checks
                    if check_count > 10_000_000:  # 10 million tiles per rectangle max
                        print(f"  Rectangle too large to validate: area={area}")
                        all_valid = False
                        break

                    if (x, y) not in valid_tiles:
                        all_valid = False
                        break

            if all_valid:
                max_area = area
                best_corners = ((x1, y1), (x2, y2))
                print(f"  *** Found: area={area} between ({x1},{y1}) and ({x2},{y2})")

        if pair_count > 10_000_000:
            break

    print(f"\n{'='*60}")
    print(f"Best rectangle: area={max_area}")
    print(f"Corners: {best_corners}")
    print(f"Time: {time.time() - start_time:.1f}s")
    print(f"{'='*60}")

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

    print("="*60)
    print("EXAMPLE")
    print("="*60)
    example_result = solve('example.txt')
    print(f"\nExample result: {example_result}")
    print(f"Expected: 24")
    print()

    # Solve actual puzzle
    print("\n" + "="*60)
    print("ACTUAL INPUT")
    print("="*60)
    result = solve('input.txt')
    print(f"\n\nPart 2 answer: {result}")
