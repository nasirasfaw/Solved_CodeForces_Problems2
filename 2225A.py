t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    
    if y > 2*x and y % (y - x) != 0:
        print("YES")
    else:
        print("NO")
