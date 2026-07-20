n = int(input())
t = list(map(int, input().split()))
t1, t2, t3 = t.count(1), t.count(2), t.count(3)
tms = min(t1, t2, t3)
tp = []
for i, x in enumerate(t):
    tp.append([x, i])
tp.sort()
gr = []
i = 0
for j in range(1, len(tp)):
    if tp[j][0] != tp[j-1][0]:
        gr.append(tp[i:j])
        i = j
gr.append(tp[i:])
mg = min(len(x) for x in gr)
print(tms)
if tms != 0:
    for i in range(mg):
        print(gr[0][i][1]+1, gr[1][i][1]+1, gr[2][i][1]+1)
