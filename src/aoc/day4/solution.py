from ..matrix import make_matrix, precompute_adjacents


def build_degrees(matrix: list[list[str]]) -> tuple[list[list[int]], int, int]:
    m = len(matrix)
    n = len(matrix[0])
    deg = [[0] * n for _ in range(m)]

    adj = precompute_adjacents(m, n)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] != "@":
                continue

            degree = 0
            for nx, ny in adj[i][j]:
                if matrix[nx][ny] == "@":
                    degree += 1

            deg[i][j] = degree

    return deg, m, n


def part_1(content: str) -> str:
    matrix = make_matrix(content)
    deg, m, n = build_degrees(matrix)

    accessible = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "@" and deg[i][j] < 4:
                accessible += 1

    return str(accessible)


def part_2(content: str) -> str:
    matrix = make_matrix(content)
    deg, m, n = build_degrees(matrix)
    adj = precompute_adjacents(m, n)

    alive = [[matrix[i][j] == "@" for j in range(n)] for i in range(m)]

    queue = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "@" and deg[i][j] < 4:
                queue.append((i, j))

    accessible = 0
    while queue:
        i, j = queue.pop(0)
        if not alive[i][j]:
            continue

        alive[i][j] = False

        for nx, ny in adj[i][j]:
            if not alive[nx][ny]:
                continue

            if matrix[nx][ny] != "@":
                continue

            deg[nx][ny] -= 1
            if deg[nx][ny] == 3:
                queue.append((nx, ny))

        accessible += 1

    return str(accessible)
