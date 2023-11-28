#!/usr/bin/python3
charr = ", "
for i in range(0, 100):
    if i < 10:
        print("{}{}".format(0, i), end=charr)
    else:
        if i == 99:
            charr = '\n'
        print(i, end=charr)
