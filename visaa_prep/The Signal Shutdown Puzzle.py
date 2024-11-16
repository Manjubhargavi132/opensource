def fix_grid(N,M,grid):
    rows_to_zero=set()
    cols_to_zero=set()
    for i in range(N):
        for j in range(M):
            if grid[i][j]==0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)
    for i in range(N):
        for j in range(M):
            if i in rows_to_zero or j in cols_to_zero:
                grid[i][j]=0
    return grid
N,M=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
fixed_grid=fix_grid(N,M,grid)
for row in fixed_grid:
    print(" ".join(map(str,row)))
