from math import gcd
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
 
    if k <= n and n % gcd(2, k) == 0:
        print("YES")
    else:
        print("NO")
