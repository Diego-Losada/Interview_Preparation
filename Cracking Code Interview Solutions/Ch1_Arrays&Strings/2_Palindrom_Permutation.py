"""
Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other.
input: hola, loah
output: True
"""

from collections import Counter

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)


print(check_permutation("hola", "loah") == True)
