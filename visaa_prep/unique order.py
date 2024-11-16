def unique_elements(n,arr):
    seen=set()
    unique=[]
    for num in arr:
        if num not in seen:
            unique.append(num)
            seen.add(num)
    print(" ".join(map(str,unique)))
n=int(input())
arr=list(map(int,input().strip().split()))
unique_elements(n,arr)
