t = int(input())
for _ in range(t):
    n = int(input())
 
    count = 0
    x = 0
    for i in range(1, 10):
        x = x*10 + 1
        for d in range(1, 10):
            if d * x <= n:
                count += 1
 
    print(count)
