import sys
from pybmstu import tex


def print_usage():
    print("usage: just use it")


def main() -> int:
    if len(sys.argv) > 1:
        if sys.argv[1] in ("tex", "latex"):
            return tex.tex_runner(sys.argv[2:])

    print_usage()
    return -1
