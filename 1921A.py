from math import sqrt
t = int(input())
for _ in range(t):
    cd = []
    for i in range(4):
        x, y = map(int, input().split()) 
        cd.append([x, y])
    ds = []
    for i in range(len(cd)):
        for j in range(len(cd)):
            if j != i:
                ds.append(sqrt((cd[i][0] - cd[j][0])**2 + (cd[i][1]-cd[j][1])**2))
    s = min(ds)
 
    print(int(s**2))
