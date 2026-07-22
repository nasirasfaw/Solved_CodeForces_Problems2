t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    i = s.index('B')
    j = s[::-1].index('B')

    answer = len(s[i:len(s)-j])

    print(answer)
