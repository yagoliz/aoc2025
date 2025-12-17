from collections import deque

from ..matrix import make_matrix


def part_1(content: str) -> str:
    matrix = make_matrix(content)
    rows, cols = len(matrix), len(matrix[0])

    queue = deque()
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # First row to find S
    S_pos = cols // 2
    queue.append((1, S_pos))

    visited[0][S_pos] = True
    visited[1][S_pos] = True

    split_count = 0
    while queue:
        i, j = queue.popleft()

        # If that ray is at the end, we forget it
        if i + 1 == rows:
            continue

        # We encounter beam splitter '^'
        if matrix[i + 1][j] == "^":
            if visited[i + 1][j]:
                continue

            visited[i + 1][j] = True

            split_count += 1

            # Left side of the beam
            left_i, left_j = i + 1, j - 1
            if not visited[left_i][left_j]:
                visited[left_i][left_j] = True
                queue.append((left_i, left_j))

            # Right side of the beam
            right_i, right_j = i + 1, j + 1
            if not visited[right_i][right_j]:
                visited[right_i][right_j] = True
                queue.append((right_i, right_j))

        # We encounter a '.'
        else:
            if not visited[i + 1][j]:
                visited[i + 1][j] = True
                queue.append((i + 1, j))

    return str(split_count)


def part_2(content: str) -> str:
    matrix = make_matrix(content)
    rows, cols = len(matrix), len(matrix[0])

    visited = [[0 for _ in range(cols)] for _ in range(rows)]

    # First row to find S
    S_pos = cols // 2

    visited[0][S_pos] = 1
    visited[1][S_pos] = 1

    for i in range(2, rows):
        for j in range(cols):
            if matrix[i][j] == "^":
                visited[i][j - 1] += visited[i - 1][j]
                visited[i][j + 1] += visited[i - 1][j]
            else:
                visited[i][j] += visited[i - 1][j]

    return str(sum(visited[-1][:]))
