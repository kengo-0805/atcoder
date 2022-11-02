n = int(input())
card = list(map(int, input().split()))
card.sort(reverse=True)
alice = 0
bob = 0
for i in range(len(card)):
    if i % 2 == 0:
        alice += card[i]
    else:
        bob += card[i]
print(alice-bob)