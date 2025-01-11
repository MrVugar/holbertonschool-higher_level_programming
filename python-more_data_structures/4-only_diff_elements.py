#!/usr/bin/python3
def only_diff_elements(set1, set2):
    return sorted(set1.symmetric_difference(set2))
