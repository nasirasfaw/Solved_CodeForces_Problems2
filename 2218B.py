t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    
    a.sort()
    
    sum1 = a[6] - sum(a[:6])
    sum2 = a[0] - sum(a[1:])

    print(max(sum1, sum2))
