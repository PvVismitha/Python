"""
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

Sample input
1222311

Sample output
(1, 1) (3, 2) (1, 3) (2, 1)
"""
from itertools import groupby

data = input('Enter a string\n')
for k, g in groupby(data, key=lambda x: x):
    group = list(g)
    print((len(group), int(k)), end=' ')
