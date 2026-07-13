n = int(input())
a = list(map(int, input().split()))
    
a.sort()
d = []
for i in range(n):
    d.append(a[n-1]-a[i])
s = sum(d)
print(s)
