# 19. Write a program to find all permutations of a smaller string within a larger string.
from itertools import permutations

s = "cbabcacab"
sub = "abc"
sub_permutations = [''.join(p) for p in permutations(sub)]
result =  [p for p in sub_permutations if p in s]
print(result)