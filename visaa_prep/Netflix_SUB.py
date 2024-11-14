A, B, C, X = map(int, input().split())

if A+C >= X or A+B >= X or B+C >= X:
    print("YES")
else:
    print("NO")
