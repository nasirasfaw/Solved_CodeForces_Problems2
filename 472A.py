n = int(input())
k = 4
while k <= n//2:
    if all((n-k) % i != 0 for i in range(2, k+1)):
        k += 2
    else:
        print(k, n-k)
        break
