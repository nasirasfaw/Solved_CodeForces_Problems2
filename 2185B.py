t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    m = max(a)
    for i in range(1, len(a)):
        if a[i] == m:
            a[0], a[i] = a[i], a[0]

    maxs = []
    for i in range(1, len(a)):
        maxs.append(max(a[:i]))
    maxs.append(max(a)) #This is to include the last max, when i = len(a)

    print(sum(maxs))
