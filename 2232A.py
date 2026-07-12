t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    a1 = []
    a2 = []
    for i in range(n):
        if a[i] < a[n//2]:
            a1.append(a[i])
        elif a[i] > a[n//2]:
            a2.append(a[i])
    answer = max(len(a1), len(a2))

    print(answer)
