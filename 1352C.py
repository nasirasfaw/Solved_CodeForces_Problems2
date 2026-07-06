t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
 
    q, r = k//(n-1), k%(n-1)
 
    if r == 0:
        answer = q * n - 1
    else:
        answer = q * n + r
 
    print(answer)
