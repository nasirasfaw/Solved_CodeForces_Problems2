t = int(input())
for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split()))

    a1 = list(set(a))

    print(len(a1))
