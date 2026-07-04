t = int(input())
for _ in range(t):
    k = int(input())
    seq = []
    for i in range(1, 1800):
        d = [int(j) for j in str(i)]
        if i % 3 != 0 and d[::-1][0] != 3:
            seq.append(i)

    print(seq[k-1])
