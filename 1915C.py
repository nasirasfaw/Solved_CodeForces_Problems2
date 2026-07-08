from math import sqrt
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if sqrt(sum(a)) == int(sqrt(sum(a))):
        print("YES")
    else:
        print("NO")
