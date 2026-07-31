t = int(input())
for _ in range(t):
    mat = []
    while len(mat) < 8:
        row = input().strip()
        if row:
            mat.append(row)

    for i in range(1, 7):
        for j in range(1, 7):
            if (mat[i][j] == '#' and 
                mat[i-1][j-1] == '#' and 
                mat[i-1][j+1] == '#'):
                print(i+1, j+1)
                break
        else:
            continue
        break
