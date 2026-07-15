from math import prod
t = int(input()) 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    a[0] = a[0] +1
    
    max_prod = prod(a) 

    print(max_prod) 
