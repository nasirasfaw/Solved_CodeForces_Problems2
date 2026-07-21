t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    if a == b:
        answer = 0
    elif (a < b and a % 2 == b % 2) or (a > b and a % 2 != b % 2):
        answer = 2
    else:
        answer = 1

    print(answer)
