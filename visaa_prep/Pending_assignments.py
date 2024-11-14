X, Y, Z = map(int, input().split())

requiredTime = X * Y
availableTime = Z * 1440

if requiredTime <= availableTime:
    print("YES")
else:
    print("NO")
