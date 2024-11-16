def rotate_array(arr,K):
    N=len(arr)
    K=K%N
    return arr[-K:]+arr[:-K]
N=int(input())
arr=list(map(int,input().split()))
K=int(input())
rotated_arr=rotate_array(arr,K)
print(" ".join(map(str,rotated_arr)))
