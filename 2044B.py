t = int(input())
for _ in range(t):
    a = input()
    a = list(a)
    b = a[::-1]

    for i in range(len(a)):
        if b[i] == 'p':
            b[i] = 'q'
        elif b[i] == 'q':
            b[i] = 'p'
    b = "".join(b)
    print(b)
