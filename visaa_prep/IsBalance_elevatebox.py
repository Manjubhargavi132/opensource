n = int(input())
a = list(map(int, input().split()))
b = []

for i in range(n):
    left_weight = sum(a[:i])
    right_weight = sum(a[i+1:])
    balance = abs(left_weight - right_weight)
    b.append(balance)

print(" ".join(map(str, b)))
