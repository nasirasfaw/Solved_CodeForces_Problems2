t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    s = input()
    
    inserted = False

    for i in range(n):
        if int(s[i]) < d:
            s = s[:i] + str(d) + s[i:]
            inserted = True
            break
    if not inserted:
        s += str(d)

    print(s)
