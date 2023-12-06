#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    scoreValue = float('-inf')
    scoreKey = None
    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > scoreValue:
            scoreValue = value
            scoreKey = key
    return scoreKey
