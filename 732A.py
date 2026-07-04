k, r = map(int, input().split())

n = 1
while True:
    if (n * k) % 10 == 0 or (n * k) % 10 == r:
        print(n)
        break
    n += 1
