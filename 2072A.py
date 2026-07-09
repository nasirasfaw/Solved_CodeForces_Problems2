t = int(input())
for _ in range(t):
    n, k, p = map(int, input().split())
    a = [0]*n
    if p*n < abs(k):
        answer = -1
    else:
        count = 0
        i = 0
        while abs(sum(a)) < abs(k):
            if k> 0:
                a[i] = p 
            else:
                a[i] = -p
            count += 1
            i += 1
        answer = count
    print(answer)
