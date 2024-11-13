t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    runs_needed = x - y + 1
    print(runs_needed)
