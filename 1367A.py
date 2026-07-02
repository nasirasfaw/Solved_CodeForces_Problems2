t = int(input())
 
for _ in range(t):
    b = input()
    b1 = ""
    i = 0
    while i < len(b):
        if i%2==0:
            b1 += b[i]
        i += 1  
    print(b1+b[-1])

#Optional: Simply print(b[::2]+b[-1]) outputs the desired result.
