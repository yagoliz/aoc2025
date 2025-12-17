from shapely.geometry import Polygon, box
from shapely.prepared import prep


def parse_content(content: str) -> list[tuple[int, int]]:
    positions = []
    for line in content.splitlines():
        positions.append(tuple(map(int, line.split(","))))
    return positions


def part_1(content: str) -> str:
    red_tiles = parse_content(content)
    nelem = len(red_tiles)

    max_area = -1
    for i in range(nelem - 1):
        for j in range(i + 1, nelem):
            pi, pj = red_tiles[i], red_tiles[j]

            area = (abs(pj[0] - pi[0]) + 1) * (abs(pj[1] - pi[1]) + 1)
            max_area = max(max_area, area)

    return str(max_area)


def part_2(content: str) -> str:
    red_tiles = parse_content(content)

    poly = Polygon(red_tiles)
    prepared_poly = prep(poly)

    nelem = len(red_tiles)
    max_area = 0

    for i in range(nelem):
        for j in range(i + 1, nelem):
            pi, pj = red_tiles[i], red_tiles[j]

            r1, r2 = min(pi[0], pj[0]), max(pi[0], pj[0])
            c1, c2 = min(pi[1], pj[1]), max(pi[1], pj[1])

            area = (r2 - r1 + 1) * (c2 - c1 + 1)

            if area <= max_area:
                continue

            # Create rectangle in (x, y) coordinates: (col, row)
            rect = box(r1, c1, r2, c2)

            # Check if rectangle is contained in or touches the polygon
            if prepared_poly.contains(rect):
                max_area = area

    return str(max_area)
