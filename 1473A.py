t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if all(x <= d for x in a) or any(a[i] + a[0] <= d for i in range(1, n)):
        print("YES")
    else:
        print("NO")
