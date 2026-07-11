t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    d = min(a[i] - a[i-1] for i in range(1, len(a)))
    if d < 0:
        answer = 0
    else:
        answer = d//2 + 1

    print(answer)
