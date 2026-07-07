t = int(input())
for _ in range(t):
    x, k = map(int, input().split())

    if x == 0:
        print(0)
        print(0)
    elif abs(x) >= abs(k) and x % k == 0:
        print(2)
        if x > 0:
            print(x-1, 1)
        else:
            print(x+1, -1)
    else:
        print(1)
        print(x)
