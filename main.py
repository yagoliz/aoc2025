import argparse
from pathlib import Path
from aoc.utils import AVAILABLE_DAYS, MODULES, read_content


def main(days: list[str], parts: list[str]):
    for day in days:
        module = MODULES[day]
        content = read_content(Path(f"input/{day}.txt"))

        for part in parts:
            if part == "1":
                result = module.part_1(content)
            elif part == "2":
                result = module.part_2(content)
            else:
                raise RuntimeError(
                    f"There are only 2 parts to this problem! You inputted {part}"
                )

            print(f"Solution {day} - Part {part}: {result}")


if __name__ == "__main__":
    # What arguments do we want
    parser = argparse.ArgumentParser(
        prog="aoc", description="AoC 2025 solver", epilog="Author - Yago Lizarribar"
    )

    # Day
    parser.add_argument(
        "-d", "--day", type=int, default=None, help="Day to be solved. (Default: all)"
    )

    # Sub part
    parser.add_argument(
        "-p",
        "--part",
        type=str,
        choices=["1", "2"],
        default=None,
        help="Solve part 1 or 2 (Default: all)",
    )

    # Our main routine
    args = parser.parse_args()

    if args.day is None:
        days = AVAILABLE_DAYS
    else:
        if f"day{args.day}" not in MODULES.keys():
            raise RuntimeError(
                f"day{args.day} is not available. You can choose from {AVAILABLE_DAYS}"
            )
        days = [f"day{args.day}"]

    if args.part is None:
        parts = ["1", "2"]
    else:
        parts = [args.part]

    main(days, parts)
