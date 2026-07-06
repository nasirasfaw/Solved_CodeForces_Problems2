t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    d1 = []
    d2 = []
    for i in range(len(a)):
        if i%2 != a[i]%2 and i%2 == 0:
            d1.append(i)
        elif i%2 != a[i]%2 and i%2 != 0:
            d2.append(i)
    if len(d1) == len(d2):
        print(len(d1))
    else:
        print(-1)
