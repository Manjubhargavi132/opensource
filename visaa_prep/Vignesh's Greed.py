def max_perimeter(sticks):
    sticks.sort(reverse=True)
    for i in range(len(sticks)-2):
        if sticks[i]<sticks[i+1]+sticks[i+2]:
            return sticks[i]+sticks[i+1]+sticks[i+2]
    return -1
N=int(input())
sticks=list(map(int,input().split()))
print(max_perimeter(sticks))
