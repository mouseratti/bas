# x = 5
# result = 1
# for pos in range(1,x+1):
#     result *= pos
# print(result)

import sys; sys.setrecursionlimit(2000) 

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

n = 1006
print(factorial(n))