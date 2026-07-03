n = int(input())
a = list(map(int, input().split()))

a.sort(reverse = True)

for i in range(n):
    if sum(a[:i]) <= sum(a[i:]) and sum(a[:i+1]) > sum(a[i+1:]):
        min_coins = len(a[:i+1])

print(min_coins)
