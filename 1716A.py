t = int(input())
for _ in range(t):
    n = int(input())

    if n == 1:
        answer = 2
    elif n == 2:
        answer = 1
    elif n % 3 == 0:
        answer = n//3
    else:
        answer = n//3 + 1  

    print(answer)
