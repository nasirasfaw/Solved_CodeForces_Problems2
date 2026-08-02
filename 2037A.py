t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    counts = [a.count(x) for x in list(set(a))]
    
    score = 0
    for i in range(len(counts)):
        score += counts[i]//2

    print(score)
