N = int(input())
m = []

for i in range(N):
    row = list(map(int, input().split()))
    m.append(row)

for i in range(N):
    print(" ".join(map(str, m[i][::-1])))
