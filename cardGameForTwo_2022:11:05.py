n = int(input())
card = list(map(int, input().split()))
card.sort(reverse=True)
ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += card[i]
    else:
        ans -= card[i]
print(ans)