t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    d = []
    for i in range(1, n):
        d.append(a[i]-a[i-1])

    dm = min(d)

    print(dm)
