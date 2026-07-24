t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    for i in range(1, len(a)-1):
        if a[i-1] == a[i] == a[i+1]:
            print(a[i])
            break
    else:
        print(-1)
