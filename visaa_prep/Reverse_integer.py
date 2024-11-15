n = int(input())
r = 0

while n != 0:
    r = r * 10 + n % 10
    n //= 10

if r < -2*31 or r > 2*31 - 1:
    print(0)
else:
    print(r)
