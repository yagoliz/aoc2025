from importlib import import_module
from pathlib import Path
from types import ModuleType

def read_content(path: Path) -> str:
    return path.read_text()

def try_import(path: str) -> ModuleType:
    root = Path(__file__).parent
    try:
        return import_module(f".{path}.solution", package="aoc")
    except:
        raise RuntimeError(f"{path} - Not available")


def list_days() -> list[str]:
    cwd = Path(__file__).parent
    result = cwd.glob("day*")
    days = [name.name for name in result]
    days.sort()
    return days


def import_modules():
    days = list_days()
    days.sort()

    for day in days:
        MODULES[day] = try_import(day)


# Global vars for import
MODULES = {}
import_modules()

AVAILABLE_DAYS = list_days()
