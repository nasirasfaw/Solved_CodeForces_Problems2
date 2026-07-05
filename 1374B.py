t = int(input())
for _ in range(t):
    n = int(input())

    a = 0 
    b = 0  
    while n % 2 == 0:
        a+= 1
        n //= 2
    while n % 3 == 0:
        b += 1
        n //= 3
    if n != 1 or a > b:
        print(-1)
    else:
        print(2 * b - a)
