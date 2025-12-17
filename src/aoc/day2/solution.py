from ..ranges import merge_ranges, in_range


def parse_ranges(content: str) -> list[tuple[int, int]]:
    return [tuple(map(int, part.split("-"))) for part in content.split(",") if part]  # type: ignore


def part_1(content: str) -> str:
    ranges = merge_ranges(parse_ranges(content))
    if not ranges:
        return "0"

    min_id = ranges[0][0]
    max_id = ranges[-1][1]

    max_digits = len(str(max_id))

    invalid_total = 0

    for d in range(1, max_digits // 2 + 1):
        start_pattern = 10 ** (d - 1)
        end_pattern = 10**d

        for pattern in range(start_pattern, end_pattern):
            s = str(pattern)
            num = int(s + s)

            if num > max_id:
                break
            if num < min_id:
                continue

            if in_range(num, ranges):
                invalid_total += num

    return str(invalid_total)


def part_2(content: str) -> str:
    ranges = merge_ranges(parse_ranges(content))
    if not ranges:
        return "0"

    min_id = ranges[0][0]
    max_id = ranges[-1][1]
    max_digits = len(str(max_id))

    invalid_total = 0
    seen = set()

    for d in range(1, max_digits):
        if 2 * d > max_digits:
            break

        start_pattern = 10 ** (d - 1)
        end_pattern = 10**d

        for pattern in range(start_pattern, end_pattern):
            s = str(pattern)

            k = 2
            while True:
                num = int(s * k)

                if num > max_id:
                    break

                elif num < min_id:
                    continue

                else:
                    if num not in seen and in_range(num, ranges):
                        seen.add(num)
                        invalid_total += num

                k += 1

    return str(invalid_total)
