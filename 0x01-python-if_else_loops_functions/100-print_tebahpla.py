#!/usr/bin/python3
i = 0
c = ord('z')
while c >= ord('a'):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
    c -= 1
