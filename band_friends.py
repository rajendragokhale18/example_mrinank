def is_interlocked(matrix, s, band_char):
    visited = [[False] * s for _ in range(s)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def dfs(x, y, parent_x, parent_y):
        if visited[x][y]:
            return True  # Found a cycle (interlock)

        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < s and 0 <= ny < s and matrix[nx][ny] in {band_char, '2' if band_char == '1' else '1'}:
                if (nx, ny) != (parent_x, parent_y):  # Avoid going back to the parent node
                    if dfs(nx, ny, x, y):
                        return True
        return False

    for i in range(s):
        for j in range(s):
            if matrix[i][j] == band_char and not visited[i][j]:
                if dfs(i, j, -1, -1):
                    return True  # Interlocked
    return False


def count_overlaps(matrix, s):
    overlap_count = 0
    for i in range(s):
        for j in range(s):
            if matrix[i][j] in {'1', '2'} and all(matrix[i][j] in {matrix[x][y] for x, y in [(i-1,j)]})
    return overlaps 
