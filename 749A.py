n = int(input())

np = n // 2

if n % 2 == 0:
    answer = [2]*np
else:
    answer = [2]*(np - 1) + [3]
    
print(np)
print(*answer)
