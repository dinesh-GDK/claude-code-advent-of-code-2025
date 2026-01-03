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

# Test with the example
example_red = [(7,1), (11,1), (11,7), (9,7), (9,5), (2,5), (2,3), (7,3)]

# Build green edge tiles
green_edge = set()
for i in range(len(example_red)):
    p1 = example_red[i]
    p2 = example_red[(i + 1) % len(example_red)]
    tiles = get_tiles_between(p1, p2)
    green_edge.update(tiles)

# Remove red tiles
red_set = set(example_red)
green_edge -= red_set

print(f"Red tiles: {len(example_red)}")
print(f"Green edge tiles: {len(green_edge)}")
print(f"Green edges: {sorted(green_edge)}")

# Check point_in_polygon for some test points
test_points = [
    (5, 4),   # Should be inside
    (3, 3),   # Should be inside
    (10, 5),  # Should be inside
    (1, 1),   # Should be outside
    (12, 8),  # Should be outside
]

for pt in test_points:
    inside = point_in_polygon(pt, example_red)
    print(f"Point {pt}: {'INSIDE' if inside else 'OUTSIDE'}")

# Now test the specific rectangle mentioned: 9,5 and 2,3 should have area 24
print("\n=== Testing rectangle (9,5) to (2,3) ===")
x1, y1 = 9, 5
x2, y2 = 2, 3

min_x, max_x = min(x1, x2), max(x1, x2)
min_y, max_y = min(y1, y2), max(y1, y2)

area = (max_x - min_x + 1) * (max_y - min_y + 1)
print(f"Area: {area}")
print(f"Bounds: x=[{min_x},{max_x}], y=[{min_y},{max_y}]")

# Check all tiles in this rectangle
all_valid = True
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        is_red = (x, y) in red_set
        is_green_edge = (x, y) in green_edge
        is_inside = point_in_polygon((x, y), example_red)
        is_valid = is_red or is_green_edge or is_inside

        if not is_valid:
            print(f"  INVALID tile at ({x},{y})")
            all_valid = False

print(f"Rectangle valid: {all_valid}")
