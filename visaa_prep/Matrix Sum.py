def calculate_sums(matrix,N):
    row_sum=[0]*N
    col_sum=[0]*N
    for i in range(N):
        for j in range(N):
            row_sum[i]+=matrix[i][j]
            col_sum[j]+=matrix[i][j]
    result=[] 
    for i in range(N):
        result.append(row_sum[i]+col_sum[i])
    return result
N=int(input())
matrix=[list(map(int,input().split())) for _ in range(N)]
result=calculate_sums(matrix,N)
print(" ".join(map(str,result)))
