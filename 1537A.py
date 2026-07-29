t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))        
    
    s = sum(a)
    if s == len(a):
        answer = 0
    elif s < len(a):
        answer = 1
    else:
        answer = s-len(a)

    print(answer)
