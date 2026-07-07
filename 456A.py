n = int(input())
p = []
for _ in range(n):
    a, b = map(int, input().split())
    p.append([a, b])

p.sort()

if all(p[i-1][1] < p[i][1] for i in range(1, n)):
    answer = "Poor Alex"
else:
    answer = "Happy Alex"

print(answer)
