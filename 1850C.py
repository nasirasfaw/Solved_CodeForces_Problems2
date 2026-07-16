t = int(input())
for t in range(t):
    grid = [input() for _ in range(8)]
    answer = []
    for i in range(8):
        for j in range(8):
            if grid[i][j] != ".":
                answer.append(grid[i][j])
    answer = "".join(answer)

    print(answer)
