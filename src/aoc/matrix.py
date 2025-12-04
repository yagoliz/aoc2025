def make_matrix(content: str) -> list[list[str]]:
    matrix = []

    for line in content.splitlines():
        matrix.append([character for character in line])

    return matrix


def get_adjacent_idx(i: int, j: int, rows: int, cols: int) -> list[tuple[int, int]]:
    
    if i < 0 or j < 0 or i >= rows or j >= cols:
        raise RuntimeError(f"Values of i,j out of bounds. Provided {i},{j} - Rows: {rows}, Cols: {cols}")

    adjacents_i = [i]
    adjacents_j = [j]
    
    if i > 0:
        adjacents_i.append(i-1)
    
    if i < rows-1:
        adjacents_i.append(i+1)

    if j > 0:
        adjacents_j.append(j-1)

    if j < cols-1:
        adjacents_j.append(j+1)
        
    adjacents = []
    for val_i in adjacents_i:
        for val_j in adjacents_j:
            if val_i == i and val_j == j:
                continue

            adjacents.append((val_i, val_j))

    return adjacents