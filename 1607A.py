t = int(input())
for _ in range(t):  
    st = input()
    s = input()
    sm = 0
    for i in range(1, len(s)):
        sm += abs(st.index(s[i]) - st.index(s[i-1]))
    print(sm)
