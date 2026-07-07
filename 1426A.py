from math import ceil
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())

    k = 1 + ceil((n-2)/x)
    if n < 3:
        print(1)
    elif n >= 3 and n < x:
        print(2)
    else:
        print(k)
