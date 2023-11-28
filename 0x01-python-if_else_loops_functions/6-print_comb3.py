#!/usr/bin/python3
charr = ", "
for i in range(0, 100):
    int1 = i / 10
    int2 = i % 10
    if i < 10 and int1 < int2:
        print("{}{}".format(0, i), end=charr)
    elif int1 < int2:
        if i == 89:
            charr = "\n"
        print(i, end=charr)
