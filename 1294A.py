t = int(input())
for _ in range(t):
    a, b, c, n = map(int, input().split())

    x = [a, b, c]
    x.sort()

    equalizer = (x[2] - x[0]) + (x[2] - x[1]) 

    if n >= equalizer and (n - equalizer) % 3 == 0:
        print("YES")
    else:
        print("NO")
