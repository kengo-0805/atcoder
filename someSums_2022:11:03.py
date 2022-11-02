def sum_keta(num):
    sum_num = 0
    while num > 0:
        keta = num % 10
        print("keta",keta)
        num //= 10
        print("num", num)
        sum_num += keta
    return sum_num

n, a, b = map(int, input().split())
ans = 0
for i in range(1,n+1):
    if a<=sum_keta(i)<=b:
        # print(sum_keta(i))
        ans += i
print(ans)