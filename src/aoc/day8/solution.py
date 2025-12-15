from aoc.linalg import distance_3d

def parse_positions(content: str) -> list[tuple[int, int, int]]:
    positions = []
    for line in content.splitlines():
        positions.append(tuple(map(int, line.split(","))))
    return positions


def get_adjacency_matrix(positions: list[tuple[int, int, int]]) -> list[list[int, int, float]]:
    nelem = len(positions)

    distances = []
    for i in range(nelem-1):
        for j in range(i+1,nelem):
            dist = distance_3d(positions[i], positions[j])
            distances.append([i, j, dist])

    return distances


def are_all_same_group(assigned: list[int]) -> bool:
    g0 = assigned[0]

    if g0 == -1:
        return False
    
    for i in range(1, len(assigned)):
        if assigned[i] != g0:
            return False

    return True


def part_1(content: str) -> str:
    # Get adjacency matrix
    positions = parse_positions(content)
    adj = get_adjacency_matrix(positions)
    adj = sorted(adj, key=lambda d: d[2])

    # Solving
    npos = len(positions)
    assigned = [-1 for _ in range(npos)]

    max_number = 1000
    group_num = 0
    k = 0
    for (i, j, dist) in adj:
        k += 1

        g0, g1 = assigned[i], assigned[j]

        if g0 == -1 and g1 == -1:
            assigned[i], assigned[j] = group_num, group_num
            group_num += 1

        elif g0 != -1 and g1 != -1:
            if g0 <= g1:
                for gswitch in range(npos):
                    if assigned[gswitch] == g1:
                        assigned[gswitch] = g0
            else:
                for gswitch in range(npos):
                    if assigned[gswitch] == g0:
                        assigned[gswitch] = g1

        else:
            if g0 == -1:
                assigned[i] = g1
            else:
                assigned[j] = g0

        if k == max_number:
            break

    # We need to sort. Probably there is a more efficient way to do these 2 steps
    groups = {}
    for assignee in assigned:
        if assignee >= 0:
            groups[assignee] = groups.get(assignee, 0) + 1
        else:
            group_num += 1
            groups[group_num] = 1

    elems = sorted(groups.items(), key=lambda it: it[1], reverse=True)[0:3]
    p = 1
    for e in elems:
        p *= e[1]

    return str(p)


def part_2(content: str) -> str:
    # Get adjacency matrix
    positions = parse_positions(content)
    adj = get_adjacency_matrix(positions)
    adj = sorted(adj, key=lambda d: d[2])


    npos = len(positions)
    assigned = [-1 for _ in range(npos)]

    group_num, result = 0, -1
    for (i, j, dist) in adj:

        g0, g1 = assigned[i], assigned[j]

        if g0 == -1 and g1 == -1:
            assigned[i], assigned[j] = group_num, group_num
            group_num += 1

        elif g0 != -1 and g1 != -1:
            if g0 <= g1:
                for l in range(npos):
                    if assigned[l] == g1:
                        assigned[l] = g0
            else:
                for l in range(npos):
                    if assigned[l] == g0:
                        assigned[l] = g1

        else:
            if g0 == -1:
                assigned[i] = g1
            else:
                assigned[j] = g0

        if are_all_same_group(assigned):
            result = positions[i][0] * positions[j][0]
            break

    return str(result)