N = int(input())
array = list(map(int, input().split()))

result = 0
for num in array:
    result ^= num

print(result)
