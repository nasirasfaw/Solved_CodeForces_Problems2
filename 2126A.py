t = int(input())
for _ in range(t):
    x = int(input())

    x1 = [int(d) for d in str(x)]

    y = min(x1[i] for i in range(len(x1)))

    print(y)
