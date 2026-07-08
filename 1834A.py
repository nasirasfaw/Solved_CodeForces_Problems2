from math import prod
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    count = 0
    i = 0
    while sum(a) < 0 or prod(a) < 0:
        a[i] = 1
        count += 1
        i += 1

    print(count)
