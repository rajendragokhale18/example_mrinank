def calculate_intensity(lines, k):
    from collections import defaultdict

    def line_intersection(line1, line2):
        x1, y1, x2, y2 = line1
        x3, y3, x4, y4 = line2
        
        # Check if lines intersect
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denominator == 0:
            return None  # Parallel lines
        
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator
        
        # Check if intersection is within both line segments
        if (min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2) and
                min(x3, x4) <= px <= max(x3, x4) and min(y3, y4) <= py <= max(y3, y4)):
            return (px, py)
        return None

    def calculate_distance(x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)

    # Find all intersections and their associated lines
    intersections = defaultdict(list)
    n = len(lines)
    
    for i in range(n):
        for j in range(i + 1, n):
            intersection = line_intersection(lines[i], lines[j])
            if intersection:
                intersections[intersection].append(lines[i])
                intersections[intersection].append(lines[j])

    # Process each intersection to calculate intensity
    total_intensity = 0
    for point, intersecting_lines in intersections.items():
        if len(intersecting_lines) // 2 == k:  # Each line is counted twice
            intensities = []
            for line in set(intersecting_lines):  # Unique lines
                x1, y1, x2, y2 = line
                px, py = point
                if (px, py) == (x1, y1) or (px, py) == (x2, y2):
                    intensities.append(0)  # Case 1
                else:
                    intensities.append(min(calculate_distance(px, py, x1, y1), calculate_distance(px, py, x2, y2)))
            total_intensity += min(intensities)

    return total_intensity


# Input Handling
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
k = int(input())

# Calculate and print the result
result = calculate_intensity(lines, k)
print(result if result > 0 else 0)
