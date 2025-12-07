def make_matrix(content: str) -> list[list[str]]:
    matrix = []

    for line in content.splitlines():
        matrix.append([character for character in line])

    return matrix


NEIGHBOURS = [
    (-1,-1), (-1, 0), (-1, 1),
    ( 0,-1),          ( 0, 1),
    ( 1,-1), ( 1, 0), ( 1, 1)
]

def get_adjacent_idx(i: int, j: int, rows: int, cols: int) -> list[tuple[int, int]]:
    
    if i < 0 or j < 0 or i >= rows or j >= cols:
        raise RuntimeError(f"Values of i,j out of bounds. Provided {i},{j} - Rows: {rows}, Cols: {cols}")

    adjacents = []
    for (nx, ny) in NEIGHBOURS:
        di, dj = i + nx, j + ny
        if 0 <= di < rows and 0 <= dj < cols:
            adjacents.append((di, dj))

    return adjacents


def precompute_adjacents(rows: int, cols: int) -> list[list[list[tuple[int, int]]]]:
    adj = [[None] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            adj[i][j] = get_adjacent_idx(i, j, rows, cols)

    return adj