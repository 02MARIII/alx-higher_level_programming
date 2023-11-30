#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("{} argument{}:".format(len(sys.argv) - 1, "" if len(sys.argv) - 1 == 1 else "s"))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{:d}: {}".format(i, arg))