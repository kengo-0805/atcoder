from cgitb import reset
from collections import defaultdict
from unittest import result
n = int(input())

num = defaultdict(int)

for i in range(n):
    s = "".join(sorted(input()))
    num[s] += 1
result = 0

for s in num:
    n = num[s]
    result += n*(n-1)//2
print(result)