q = int(input())
for _ in range(q):
    n = int(input())
    s, t = input().split()

    s1 = ""
    for x in s:
        if x in t and t.count(x) == s.count(x):
            s1 += x
    if s1 == s:
        print("YES")
    else:
        print("NO")
