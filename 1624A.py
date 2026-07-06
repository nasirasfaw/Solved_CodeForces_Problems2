t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    d = a[len(a)-1] - a[0]
            
    print(d)
