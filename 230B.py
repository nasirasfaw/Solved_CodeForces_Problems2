from math import isqrt
lm = 10**6

prime = [True]*(lm +1)
prime[0] = prime[1] = False

for i in range(2, isqrt(lm)+1):
    if prime[i]:
        for j in range(i*i, lm +1, i):
            prime[j] = False

n = int(input())
a = list(map(int, input().split()))
for m in a:
    r = isqrt(m)
    if r * r == m and prime[r]:
        print("YES")
    else:
        print("NO")
