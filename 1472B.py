t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    c1 = a.count(1)
    c2 = a.count(2)
    if (c1 % 2 != 0) or (c1 == 0 and c2 % 2 != 0):
        print("NO")
    else:
        print("YES")
