#!/usr/bin/python3
import sys


def main():
    """Print the addition of all arguments."""

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))


if __name__ == "__main__":
    main()
