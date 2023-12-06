#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni = set()
    for element in my_list:
        if isinstance(element, int):
            uni.add(element)
    result = sum(uni)
    return result
