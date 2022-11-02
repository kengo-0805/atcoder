n = int(input())
a = list(map(int, input().split()))

flag = True

cnt = 0

while True:

    for i in range(n):
        if a[i] % 2 == 1:
            flag = False
    if flag == False:
        break
    for i in range(n):
        a[i] //= 2
    cnt += 1
print(cnt)