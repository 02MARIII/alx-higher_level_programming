#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            i += 1
        except IndexError:
            continue
    print()
    return i
