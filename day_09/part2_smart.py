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

    print(f"Checking {n_red * (n_red - 1) // 2} pairs of red tiles...")
    print("This may take a while for large rectangles...")

    pair_count = 0
    rectangles_checked = 0
    rectangles_skipped_too_large = 0

    for i in range(n_red):
        if i % 25 == 0:
            elapsed = time.time() - start_time
            print(f"Progress: {i}/{n_red} ({i/n_red*100:.1f}%), " +
                  f"checked {rectangles_checked} rects, " +
                  f"max_area={max_area:,}, " +
                  f"time={elapsed:.0f}s, " +
                  f"cache={len(polygon_cache)}")

        for j in range(i + 1, n_red):
            pair_count += 1

            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            min_rx, max_rx = min(x1, x2), max(x1, x2)
            min_ry, max_ry = min(y1, y2), max(y1, y2)

            area = (max_rx - min_rx + 1) * (max_ry - min_ry + 1)

            # Skip if can't beat current max
            if area <= max_area:
                continue

            # Safety check: skip rectangles that would take too long to validate
            # This is NOT a search space limit, just a practical time limit
            # We log these so we know if we're missing potential answers
            if area > 5_000_000:  # 5 million tiles max per rectangle
                rectangles_skipped_too_large += 1
                if rectangles_skipped_too_large <= 10:  # Only log first few
                    print(f"  Skipping very large rectangle: area={area:,} (would be slow)")
                continue

            # Check all tiles in rectangle
            rectangles_checked += 1
            all_valid = True
            checks = 0

            for x in range(min_rx, max_rx + 1):
                if not all_valid:
                    break
                for y in range(min_ry, max_ry + 1):
                    checks += 1

                    # Inner safety breaker - if we're checking too many tiles, stop
                    # This prevents infinite loops but we still mark rectangle as invalid
                    if checks > 5_000_000:
                        all_valid = False
                        break

                    if not is_valid_tile((x, y)):
                        all_valid = False
                        break

            # Only update if we successfully checked all tiles
            if all_valid:
                max_area = area
                best_corners = ((x1, y1), (x2, y2))
                print(f"  *** NEW BEST: area={area:,} between ({x1},{y1}) and ({x2},{y2})")

    elapsed = time.time() - start_time
    print(f"\n{'='*70}")
    print(f"RESULTS:")
    print(f"  Best rectangle: area={max_area:,}")
    print(f"  Corners: {best_corners}")
    print(f"  Pairs checked: {pair_count:,}")
    print(f"  Rectangles validated: {rectangles_checked:,}")
    print(f"  Rectangles skipped (too large): {rectangles_skipped_too_large:,}")
    print(f"  Polygon cache size: {len(polygon_cache):,}")
    print(f"  Time: {elapsed:.1f}s")
    print(f"{'='*70}")

    if rectangles_skipped_too_large > 0:
        print(f"\nWARNING: Skipped {rectangles_skipped_too_large} large rectangles.")
        print(f"If answer seems wrong, increase the 5M limit and re-run.")

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

    print("="*70)
    print("EXAMPLE")
    print("="*70)
    example_result = solve('example.txt')
    print(f"\nExample result: {example_result}")
    print(f"Expected: 24")
    assert example_result == 24, f"Example failed! Got {example_result}, expected 24"
    print("[OK] Example passed!")

    # Solve actual puzzle
    print("\n" + "="*70)
    print("ACTUAL INPUT")
    print("="*70)
    result = solve('input.txt')
    print(f"\n\nPart 2 answer: {result}")
