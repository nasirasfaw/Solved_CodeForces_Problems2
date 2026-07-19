import string
s = input()
chs = list(string.ascii_lowercase)
d1 = abs(chs.index(s[0]) - chs.index('a'))
 
count = min(d1, 26-d1)
for i in range(1, len(s)):
    d = abs(chs.index(s[i]) - chs.index(s[i-1]))
    count += min(d, 26-d)
 
print(count)
