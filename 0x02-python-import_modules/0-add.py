#!/usr/bin/python3
if __name__ == "__main__":
    add_import = __import__("add_0")
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add_import.add(a, b)))
