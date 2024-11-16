N=int(input())
matrix=[]
for _ in range(N):
    row=list(map(int,input().split()))
    matrix.append(row)
for j in range(N):
    for i in range(N):
        print(matrix[i][j],end=" ")
    print()    
    
