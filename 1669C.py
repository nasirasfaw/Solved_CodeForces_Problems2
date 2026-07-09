t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    x = all(a[i] % 2 == a[0] % 2 for i in range(0, len(a), 2)) #Elements with even indices have same parity
    y = all(a[i] % 2 == a[1] % 2 for i in range(1, len(a), 2)) #Elements with odd indices have same parity

    if x and y :
        answer = "YES"
    else:
        answer = "NO"

    print(answer)
