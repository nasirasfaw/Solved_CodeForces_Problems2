t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
 
    while "()" in s:
        s = s.replace("()", "")
    mn_moves = len(s)//2
    print(mn_moves)
