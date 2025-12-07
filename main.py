import argparse
from functools import partial
from pathlib import Path
import timeit

from aoc.utils import AVAILABLE_DAYS, MODULES, read_content


def main(days: list[str], parts: list[str], perf: bool, n_times: int = 10):
    for day in days:
        module = MODULES[day]
        content = read_content(Path(f"./input/{day}.txt"))

        for part in parts:
            if part == "1":
                func = module.part_1
            elif part == "2":
                func = module.part_2
            else:
                raise RuntimeError(
                    f"There are only 2 parts to this problem! You inputted {part}"
                )
            
            result = func(content)
            print(f"Solution {day} - Part {part}: {result}")

            if perf:
                timer = timeit.Timer(partial(func, content))
                elapsed = timer.timeit(n_times) / n_times

                print(f"\t- Average Time: {elapsed} over {n_times} runs")


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

    # Analyze Timing
    parser.add_argument(
        "--perf",
        action="store_true",
        help = "Time the execution of the solution"
    )

    parser.add_argument(
        "--n-times",
        type=int,
        default=10,
        help="How many runs to calculate the function timing"
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

    perf = False
    if args.perf is not None:
        perf = True

    n_times = args.n_times

    main(days, parts, perf, n_times)
