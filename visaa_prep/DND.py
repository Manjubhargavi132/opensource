N, m = map(int, input().split())
array= list(map(int, input().split()))

num1 = sum(x for x in array if x % m != 0)
num2 = sum(x for x in array if x % m == 0)

print(num2 - num1)
