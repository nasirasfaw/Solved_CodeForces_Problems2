t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    i = 0
    j = n-1
    while i < j and ((s[i] == "1" and s[j] == "0") or (s[i] == "0" and s[j] == "1")):
        i += 1
        j -= 1
    s = s[i:j+1]  

    print(len(s))
