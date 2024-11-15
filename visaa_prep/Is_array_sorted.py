n = int(input())
array = list(map(int, input().split()))

isSorted = all(array[i] <= array[i + 1] for i in range(n - 1))

print("true" if isSorted else "false")
