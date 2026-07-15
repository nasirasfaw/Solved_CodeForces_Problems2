n, k = map(int, input().split())
y = list(map(int, input().split()))

possibles = []

for i in range(n):
    if y[i] <= 5 - k:
        possibles.append(y[i])

answer = len(possibles)//3

print(answer)
