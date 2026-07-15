n = int(input())

if n >= 0:
    print(n)
else:
    n1 = abs(n)
    n1 = [d for d in str(n1)]
    if int(n1[len(n1)-1]) >= int(n1[len(n1)-2]):
        del n1[-1]
    else:
        del n1[-2]

    n1 = "".join(n1)

    print(-int(n1))
