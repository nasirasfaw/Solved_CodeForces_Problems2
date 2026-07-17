a, b = map(int, input().split())

hours = 0
used = 0
while a > 0:
    hours += a
    used += a
    a = used // b
    used = used % b

print(hours)
