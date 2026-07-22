t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    s3 = input()

    s = [s1, s2, s3]

    for x in ['A', 'B', 'C']:
        for i in range(3):
            if x not in s[i]:
                print(x)
