from ..ranges import merge_ranges, in_range


def part_1(content: str) -> str:
    [summary, numbers] = list(content.split("\n\n"))

    intervals: list[tuple[int, int]] = []
    for line in summary.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = line.split("-")
        start, end = int(a), int(b)
        if end < start:
            start, end = end, start
        intervals.append((start, end))

    ranges = merge_ranges(intervals)

    fresh = 0
    for product in numbers.splitlines():
        product = int(product)
        if in_range(product, ranges):
            fresh += 1

    return str(fresh)


def part_2(content: str) -> str:
    [summary, _] = list(content.split("\n\n"))

    intervals: list[tuple[int, int]] = []
    for line in summary.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = line.split("-")
        start, end = int(a), int(b)
        if end < start:
            start, end = end, start
        intervals.append((start, end))

    intervals.sort(key=lambda r: r[0])

    merged: list[tuple[int, int]] = []
    for start_val, end_val in intervals:
        if not merged:
            merged.append((start_val, end_val))
        else:
            last_start, last_end = merged[-1]

            # No overlapping
            if start_val > last_end:
                merged.append((start_val, end_val))

            # Any overlapping in ranges
            else:
                merged[-1] = (last_start, max(end_val, last_end))

    return str(sum(end_val - start_val + 1 for start_val, end_val in merged))
