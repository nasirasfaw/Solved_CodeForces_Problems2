n, t = map(int, input().split())

n1 = t
m = [1]*(n-1)+[0]
m1 = 0
for i in range(1, n):
    n1 += t*10**(n-i)
for i in range(n):
    m1 += m[i]*10**(n-1-i)

if n == 1 and t == 10:
    answer = -1
elif t == 10:
    answer = m1
else:
    answer = n1
print(answer)
