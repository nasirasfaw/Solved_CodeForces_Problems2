t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    m = max(s)
    d = []
    d2 = []
    for i in range(n):
        d.append(s[i] - m)
    if s.count(m) > 1 and s.count(m) < n:
        print(*d) 
    elif s.count(m) == 1:
        for i in range(n):
            if s[i] != m:
                d2.append(s[i] - m)
        for i in range(len(d)):
            if d[i] == 0:
                d[i] = abs(max(d2))
        print(*d)
    else:
        print(*[0]*n)
