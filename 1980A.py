t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = input()

    ca, cb, cc, cd, ce, cf, cg = a.count('A'), a.count('B'), a.count('C'), a.count('D'), a.count('E'), a.count('F'), a.count('G')

    counts = [ca, cb, cc, cd, ce, cf, cg]

    np = []
    for i in range(len(counts)):
        if counts[i] < m:
            np.append(m - counts[i])
    answer = sum(np)

    print(answer)
