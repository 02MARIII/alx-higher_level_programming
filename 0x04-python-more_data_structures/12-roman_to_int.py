#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev_value = 0

    if isinstance(roman_string, str) and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            current_value = val[roman_string[c]]
            if current_value >= prev_value:
                res += current_value
            else:
                res -= current_value
            prev_value = current_value
    return res
