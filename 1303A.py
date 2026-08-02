t = int(input())
for _ in range(t):
    s = input()

    if '1' not in s:
        answer = 0
    else:
        i1 = s.index('1')
        i2 = s[::-1].index('1')

        s2 = s[i1:len(s)-i2]
        answer = s2.count('0')

    print(answer)
