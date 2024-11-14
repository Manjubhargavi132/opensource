import math

X, N = map(int, input().split())
currentCapacity = 100 * X

if N <= currentCapacity:
    print(0)
else:
    remainingPassengers = N - currentCapacity
    newPlanes = math.ceil(remainingPassengers / 100)
    print(newPlanes)
