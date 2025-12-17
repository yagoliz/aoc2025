def parse_input(content: str) -> tuple[int, int, list[int]]:
    input_data = content.split("\n\n")[-1]

    grids = []
    for line in input_data.splitlines():
        grid, numbers = line.split(":")

        width, height = map(int, grid.split("x"))
        numbers = list(map(int, numbers.strip().split(" ")))

        grids.append((width, height, numbers))

    return grids


# This is such a "troll" experience
def part_1(content: str) -> str:
    grids = parse_input(content)

    total = 0
    for i, (width, height, numbers) in enumerate(grids):
        piece_area = 9 * sum(numbers)

        if width * height >= piece_area:
            total += 1

    return str(total)


def part_2(content: str) -> str:
    return "0"
