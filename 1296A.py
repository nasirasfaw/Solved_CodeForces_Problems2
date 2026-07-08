t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if all(a[i] % 2 == 0 for i in range(n)) or (len(a) % 2 == 0 and all(a[i] % 2 != 0 for i in range(n))):
        answer = "NO"
    else:
        answer = "YES"
    print(answer)
