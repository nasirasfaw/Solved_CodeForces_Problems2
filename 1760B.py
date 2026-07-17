import string
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    letters = list(string.ascii_lowercase)

    best = 0
    for ch in s:
        best = max(best, letters.index(ch)+1)

    print(best)
