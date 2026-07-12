t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    b.sort(reverse=True)

    b1 = [b[0], b[1]]

    for i in range(2, len(b)): 
        b1.append(b[i-2] % b[i-1])
        
    if b1 == b:
        print(b[0], b[1])
    else:
        print(-1) 
