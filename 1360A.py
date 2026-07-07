t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    c = max(a, b) 
    d = min(a, b)
    
    s = max(c, 2*d)

    print(s**2)
