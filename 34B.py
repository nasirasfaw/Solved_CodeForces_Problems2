n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
neg = []
for i in range(n):
    if a[i] <= 0:
        neg.append(a[i])
if m <= len(neg):
    mx_sum = 0 - sum(a[:m])
else:
    mx_sum = 0 - sum(a[:len(neg)])

print(mx_sum)
