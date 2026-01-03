def parse_input(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    # Parse shapes
    shapes = {}
    i = 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        line_stripped = lines[i].strip()
        if ':' in line_stripped and line_stripped[0].isdigit():
            # Check if this is a shape or region
            parts = lines[i].split(':')
            if 'x' in parts[0]:
                # This is a region, stop parsing shapes
                break
            # This is a shape
            shape_id = int(parts[0])
            shape_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() and ':' not in lines[i]:
                shape_lines.append(lines[i])
                i += 1
            # Convert to set of (row, col) coordinates
            coords = set()
            for r, line in enumerate(shape_lines):
                for c, ch in enumerate(line):
                    if ch == '#':
                        coords.add((r, c))
            shapes[shape_id] = coords
        else:
            i += 1

    # Parse regions
    regions = []
    for line in lines:
        if 'x' in line and ':' in line:
            parts = line.split(':')
            dims = parts[0].strip()
            width, height = map(int, dims.split('x'))
            quantities = list(map(int, parts[1].strip().split()))
            regions.append((width, height, quantities))

    return shapes, regions


def get_all_transformations(shape):
    """Generate all unique rotations and flips of a shape."""
    transformations = []

    # Get all coordinates
    coords = list(shape)
    if not coords:
        return [set()]

    # Normalize to origin (top-left at 0,0)
    def normalize(coords_set):
        if not coords_set:
            return set()
        min_r = min(r for r, c in coords_set)
        min_c = min(c for r, c in coords_set)
        return frozenset((r - min_r, c - min_c) for r, c in coords_set)

    # Generate transformations
    seen = set()

    for flip in [False, True]:
        for rotation in range(4):
            transformed = set(shape)

            # Flip horizontally
            if flip:
                max_c = max(c for r, c in transformed)
                transformed = {(r, max_c - c) for r, c in transformed}

            # Rotate (rotation * 90 degrees clockwise)
            for _ in range(rotation):
                # Rotate 90 degrees: (r, c) -> (c, -r)
                max_r = max(r for r, c in transformed)
                transformed = {(c, max_r - r) for r, c in transformed}

            # Normalize
            norm = normalize(transformed)
            if norm not in seen:
                seen.add(norm)
                transformations.append(set(norm))

    return transformations


def can_place(shape, row, col, width, height, occupied):
    """Check if shape can be placed at (row, col) in the grid."""
    for r, c in shape:
        new_r, new_c = row + r, col + c
        # Check bounds
        if new_r < 0 or new_r >= height or new_c < 0 or new_c >= width:
            return False
        # Check if occupied
        if (new_r, new_c) in occupied:
            return False
    return True


def place_shape(shape, row, col, occupied):
    """Place shape at (row, col) and return new occupied set."""
    new_occupied = occupied.copy()
    for r, c in shape:
        new_occupied.add((row + r, col + c))
    return new_occupied


def solve_region(shapes, width, height, quantities):
    """Try to fit all presents into the region using backtracking."""
    # Build list of presents to place
    presents = []
    for shape_id, quantity in enumerate(quantities):
        for _ in range(quantity):
            presents.append(shape_id)

    if not presents:
        return True

    # Check total area - quick fail if impossible
    total_area = sum(len(shapes[shape_id]) for shape_id in presents)
    if total_area > width * height:
        return False

    # Generate all transformations for each shape
    shape_transforms = {}
    for shape_id in set(presents):
        shape_transforms[shape_id] = get_all_transformations(shapes[shape_id])

    # Sort presents by area (largest first) for better pruning
    presents.sort(key=lambda sid: len(shapes[sid]), reverse=True)

    def backtrack(present_idx, occupied):
        if present_idx == len(presents):
            return True

        shape_id = presents[present_idx]

        # Try all transformations
        for transform in shape_transforms[shape_id]:
            # Get bounds of transform
            max_r = max(r for r, c in transform) if transform else 0
            max_c = max(c for r, c in transform) if transform else 0

            # Try positions more efficiently - only valid starting positions
            for row in range(height - max_r):
                for col in range(width - max_c):
                    if can_place(transform, row, col, width, height, occupied):
                        new_occupied = place_shape(transform, row, col, occupied)
                        if backtrack(present_idx + 1, new_occupied):
                            return True

        return False

    return backtrack(0, set())


def solve(filename):
    shapes, regions = parse_input(filename)

    count = 0
    for idx, (width, height, quantities) in enumerate(regions):
        if solve_region(shapes, width, height, quantities):
            count += 1
        if (idx + 1) % 100 == 0:
            print(f"Processed {idx + 1}/{len(regions)} regions, {count} valid so far")

    return count


# Test with example
example = """0:
###
.##
..#

1:
#.#
###
#.#

2:
.##
###
##.

3:
..#
###
###

4:
###
#..
###

5:
#.#
###
##.

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

with open('example.txt', 'w') as f:
    f.write(example)

result_example = solve('example.txt')
print(f"Example result: {result_example}")
print(f"Expected: 2")

# Solve actual puzzle
result = solve('day_12/input.txt')
print(f"Part 1 answer: {result}")
