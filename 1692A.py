t = int(input())
for _ in range(t):
   a, b, c, d = map(int, input().split())
   if a == min(a, b, c, d):
      answer = 3
   elif a == max(a, b, c, d):
      answer = 0
   elif b > a > max(c, d) or c > a > max(b, d) or d > a > max(c, b):
      answer = 1
   elif b < a < min(c, d) or c < a < min(b, d) or d < a < min(c, b):
      answer = 2

   print(answer)
