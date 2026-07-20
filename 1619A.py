t = int(input())
for _ in range(t):
    s = input()
    k = len(s)//2

    if len(s) % 2 == 0 and s[:k] == s[k:]:
        print("YES")
    else:
        print("NO")
