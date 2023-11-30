#!/usr/bin/python3
add_import = __import__("add_0")
a = 1
b = 2
print("{} + {} = {}".format(a, b, add_import.add(a, b)))
