x = int(input())
 
x1 = [int(d) for d in str(x)]
 
for i in range(len(x1)):
    if x1[i] > 9 - x1[i]:
        x1[i] = 9 - x1[i]
x2 = [str(k) for k in x1]
if x2[0] == '0':
    x2[0] = '9'
x3 = "".join(x2)
 
print(int(x3))
