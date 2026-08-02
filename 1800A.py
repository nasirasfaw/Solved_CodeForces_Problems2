t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    s = s.lower()
    s1 = []
    i = 0
    for j in range(1, len(s)):
        if s[j] != s[j-1]:
            s1.append(s[i:j])
            i = j
    s1.append(s[i:])

    if len(s1) == 4 and 'm' in s1[0] and 'e' in s1[1] and 'o' in s1[2] and 'w' in s1[3]:
        print("YES")
    else:
        print("NO")
