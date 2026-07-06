t = int(input())
for _ in range(t):
    a, b = input().split()
 
    a1 = list(a)
    b1 = list(b)
    a1[0], b1[0] = b1[0], a1[0]
    a1 = "".join(a1)
    b1 = "".join(b1)
 
    print(a1, b1)
