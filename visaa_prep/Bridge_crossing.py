x, y, z = map(int, input().split())

if y > z:
    print(0)
else:
    maxMangoes = (z - y) // x
    print(maxMangoes)
