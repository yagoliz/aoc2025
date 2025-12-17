def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges.sort(key=lambda r: r[0])

    merged: list[tuple[int, int]] = []
    for start_val, end_val in ranges:
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

    return merged


def in_range(x: int, ranges: list[tuple[int, int]]) -> bool:
    lo, hi = 0, len(ranges)

    while lo < hi:
        mid = (lo + hi) // 2
        start, end = ranges[mid]
        if x < start:
            hi = mid
        elif x > end:
            lo = mid + 1
        else:
            return True

    return False
