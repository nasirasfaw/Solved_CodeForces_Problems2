t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(len(a)):
        if any(a.count(a[i]) > 1 for i in range(len(a))):
            answer = "NO"
        else:
            answer = "YES"

    print(answer)
