import numpy as np
from scipy.optimize import milp, LinearConstraint


def parse_matrix(machine: str) -> tuple[list[list[int]], list[int]]:
    split_machine = machine.split(" ")

    lights = split_machine[0]
    buttons = split_machine[1:-1]

    # Processing the lights
    lights = lights.replace("[","")
    lights = lights.replace("]","")
    nrows = len(lights)
    b = [0] * nrows
    for i, char in enumerate(lights):
        if char == "#":
            b[i] = 1

    # Processing the buttons
    ncols = len(buttons)
    A = [[0] * ncols for _ in range(nrows)]

    for j, button in enumerate(buttons):
        values = button.replace("(","")
        values = values.replace(")","")
        values = values.split(",")
        for value in values:
            A[int(value)][j] = 1

    return (A, b)


def parse_matrix_2(machine: str) -> tuple[list[list[int]], list[int]]:
    split_machine = machine.split(" ")

    lights = split_machine[-1]
    buttons = split_machine[1:-1]

    # Processing the lights
    lights = lights.replace("{","")
    lights = lights.replace("}","")
    lights = lights.split(",")
    nrows = len(lights)
    b = [0] * nrows
    for i, char in enumerate(lights):
        b[i] = int(char)

    # Processing the buttons
    ncols = len(buttons)
    A = [[0] * ncols for _ in range(nrows)]

    for j, button in enumerate(buttons):
        values = button.replace("(","")
        values = values.replace(")","")
        values = values.split(",")
        for value in values:
            A[int(value)][j] = 1

    return (A, b)


def gaussian_elim_gf2(A: list[list[int]], b: list[int]) -> tuple[list[int], bool]:
    n_rows = len(A)
    n_cols = len(A[0])

    pivot_col = [-1] * n_rows
    row = 0   # current row to place pivot

    for col in range(n_cols):
        # find a pivot row with A[r][col] == 1, r >= row
        pivot_row = -1
        for r in range(row, n_rows):
            if A[r][col] == 1:
                pivot_row = r
                break

        if pivot_row == -1:
            continue   # no pivot in this column

        # swap pivot_row with current 'row'
        A[pivot_row], A[row] = A[row], A[pivot_row]
        b[pivot_row], b[row] = b[row], b[pivot_row]

        pivot_col[row] = col

        # We eliminate 1's from all other columns
        for r in range(n_rows):
            if r != row and A[r][col] == 1:
                # row r := row r XOR row 'row'
                for c in range(col, n_cols):
                    A[r][c] = A[r][c] ^ A[row][c]
                b[r] = b[r] ^ b[row]

        row = row + 1
        if row == n_rows:
            break

    # Inconsistency checks
    for r in range(n_rows):
        all_zero = True
        for c in range(n_cols):
            if A[r][c] == 1:
                all_zero = False
                break
        if all_zero and b[r] == 1:
            return (pivot_col, False)  # no solution

    return (pivot_col, True)


def build_solution_and_nullspace(A: list[list[int]], b: list[int], pivot_col: list[int]) -> tuple[list[int], list[list[int]]]:
    n_rows = len(A)
    n_cols = len(A[0])

    # which columns are pivot?
    is_pivot_col = [False] * n_cols
    for r in  range(n_rows):
        if pivot_col[r] != -1:
            is_pivot_col[pivot_col[r]] = True

    free_cols = []
    for c in range(n_cols):
        if not is_pivot_col[c]:
            free_cols.append(c)

    # particular solution: set all free vars = 0
    x0 = [0] * n_cols

    # for each pivot row r: pivot variable = b[r] (since free vars are 0)
    for r in range(n_rows):
        pc = pivot_col[r]
        if pc == -1:
            continue
        x0[pc] = b[r]   # because A is in RREF-like form now

    # nullspace basis
    # For each free column f, construct a vector v with:
    #   free var f = 1, other free vars = 0, pivot vars determined from rows
    basis = []

    for f in free_cols:
        v = [0] * n_cols
        v[f] = 1

        # For each pivot row, solve pivot var in homogeneous system (rhs = 0)
        # Row equation: x_pc XOR sum(free c with A[r][c]==1) x_c = 0
        for r in range(n_rows):
            pc = pivot_col[r]
            if pc == -1:
                continue

            # compute XOR over free vars appearing in this row
            sum_val = 0
            for c in free_cols:
                if A[r][c] == 1:
                    sum_val = sum_val ^ v[c]

            v[pc] = sum_val  # in homogeneous system, rhs=0

        basis.append(v)

    return x0, basis


def count_ones(vec: list[int]) -> int:
    return sum(vec)


def min_presses(A: list[list[int]], b: list[int]) -> int:
    pivot_col, ok = gaussian_elim_gf2(A, b)
    if not ok:
        return 10000000000

    x0, basis = build_solution_and_nullspace(A, b, pivot_col)

    d = len(basis)

    # Edge case: no free variables
    if d == 0:
        return count_ones(x0)

    best = 10000000000

    n_cols = len(A[0])

    # Enumerate all 2^d combinations
    for mask in range(1<<d):
        # Start from the particular solution
        x = x0.copy()

        # Add each basis vector where mask bit is 1
        for i in range(d):
            if ((mask >> i) & 1) == 1:
                # x := x XOR basis[i]
                for c in range(n_cols):
                    x[c] = x[c] ^ basis[i][c]

        presses = count_ones(x)
        if presses < best:
            best = presses

    return best


def part_1(content: str) -> str:
    total = 0
    for machine in content.splitlines():
        A, b = parse_matrix(machine)
        total += min_presses(A, b)

    return str(total)


def part_2(content: str) -> str:
    total = 0
    for machine in content.splitlines():
        A, b = parse_matrix_2(machine)
        constraints = LinearConstraint(A, b, b)
        c = np.ones(len(A[0]))
        res = milp(c=c, constraints=constraints, integrality=c)
        total += np.sum(res.x)

    return str(int(total))