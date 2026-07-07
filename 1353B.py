t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    a.sort()
    b.sort()
    ak, bk = a[:k], b[n-k:]
    bk = bk[::-1]
    mak = []
    for i in range(len(ak)):
        mak.append(max(ak[i], bk[i]))
 
    answer = sum(mak) + sum(a[k:])
 
    print(answer)
