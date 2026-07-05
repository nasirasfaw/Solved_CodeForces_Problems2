t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
 
    d = [a[0]]
    for i in range(1, n):
        d.append(a[i]-a[i-1])
 
    d.append(2*(x - a[n-1]))
 
    min_volume = max(d)
 
    print(min_volume)
