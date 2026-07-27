t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    ok = False

    if (a+c) % 2 == 0:
        b1 = (a+c)//2
        if b1 > 0 and b1 % b == 0:
            ok = True
    c1 = 2*b - a
    if c1 > 0 and c1 % c == 0:
        ok = True
    a1 = 2*b - c
    if a1 > 0 and a1 % a == 0:
        ok = True
      
    print("YES" if ok else "NO")
