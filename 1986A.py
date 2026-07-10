t = int(input())
for _ in range(t):
    x1, x2, x3 = map(int, input().split())
    
    x = [x1, x2, x3]
    min_sum = max(x) - min(x)
    
    print(min_sum)

#For an integer a, the minimum of sum(x1-a, x2-a, x3-a) is when a == the middle one of x1, x2 and x3.
