t = int(input())

for _ in range(t):
    x,n = map(int, input().split())
    score = (x // 10) * n
    print(score)
