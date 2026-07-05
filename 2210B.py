t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
 
    count = 0
    for i in range(len(p)):
        if p[i] <= i+1:
            count += 1
 
    print(count)
