from ..matrix import get_adjacent_idx, make_matrix

def part_1(content: str) -> str:
    matrix = make_matrix(content)

    m = len(matrix)
    n = len(matrix[0])

    accessible = 0
    for i in range(m):
        for j in range(n):
            neighbors = get_adjacent_idx(i, j, m, n)

            if matrix[i][j] != '@':
                continue

            count = 0
            for (nx, ny) in neighbors:
                if matrix[nx][ny] == '@':
                    count += 1
            
            if count < 4:
                accessible += 1

    return str(accessible)


def part_2(content: str) -> str:
    matrix = make_matrix(content)

    m = len(matrix)
    n = len(matrix[0])

    accessible = 0

    changed = True
    while changed:
        changed = False
        tmp_matrix = matrix
        for i in range(m):
            for j in range(n):
                neighbors = get_adjacent_idx(i, j, m, n)

                if matrix[i][j] != '@':
                    continue

                count = 0
                for (nx, ny) in neighbors:
                    if matrix[nx][ny] == '@':
                        count += 1
                
                if count < 4:
                    accessible += 1
                    tmp_matrix[i][j] = '.'
                    changed = True

        if changed:
            matrix = tmp_matrix
    
    return str(accessible)