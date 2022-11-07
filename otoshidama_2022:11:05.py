n, y = map(int, input().split())
x, y, z = -1, -1, -1
for i in range(n+1):
    for j in range(n+1):
        k = n-i-j
        if k > n or k < 0:
            continue

        if 10000*i + 5000*j + 1000*k == y:
            x, y, z = i, j, k
print(x, y, z)