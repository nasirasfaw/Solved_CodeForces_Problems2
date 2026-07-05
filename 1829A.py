t = int(input())
for _ in range(t):
    s = input()
    c = "codeforces"
    count = 0
    for i in range(len(s)):
        if s[i] != c[i]:
            count += 1

    print(count)
