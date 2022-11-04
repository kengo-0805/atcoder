n, y = map(int, input().split())
a, b, d = -1, -1, -1
for i in range(n+1):
    for j in range(n+1):
        c = n-i-j
        if c > n or c < 0:
            continue

        if 10000*i + 5000*j + 1000*c == y:
            a, b, d = i, j, c
print(a, b, d)