t = int(input())
for _ in range(t):
    n = int(input())   
    # c1 + 2*c2 = n so that c1-c2 <= 1 or c2-c1 <= 1
    if n % 3 == 0:
        c1 = c2 = n//3
    elif n % 3 == 1:
        c1 = 1 + n//3
        c2 = n//3
    else:
        c1 = n//3
        c2 = 1 + n//3

    print(c1, c2)
