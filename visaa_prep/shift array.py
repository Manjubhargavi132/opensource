N=int(input())
arr=list(map(int,input().split()))
rotated_array=arr[1:]+arr[:1]
print(*rotated_array)
