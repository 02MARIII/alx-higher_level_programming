#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("{}{}".format(0, i), end=", ")
    else:
        if i == 99:
            print(i, end="\n")
        else:
            print(i, end=", ")
