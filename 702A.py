n = int(input())
a = list(map(int, input().split()))

groups = []

i = 0
for j in range(1, len(a)):
    if a[j] <= a[j-1]:
        groups.append(a[i:j])
        i = j
groups.append(a[i:])
max_incr = max(len(x) for x in groups)
print(max_incr)
