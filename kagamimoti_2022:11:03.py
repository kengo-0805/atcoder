from collections import defaultdict
m = 101

n = int(input())

exist = [0]*m

for i in range(n):
    d = int(input())
    exist[d] = 1
print(sum(exist))