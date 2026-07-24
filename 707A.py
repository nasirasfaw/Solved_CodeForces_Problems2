n, m = map(int, input().split())

colors1 = {'B', 'W', 'G'}
colors2 = {'Y', 'M', 'C'}

a = []
for i in range(n):
    a.append(list(map(str, input().split())))

if all(len(set(a[i]) & colors2) == 0 for i in range(len(a))):
    print("#Black&White")
else:
    print("#Color")
