n = int(input())

if 3 <= n <= 5:
    print("Spring")
elif 6 <= n <= 8:
    print("Summer")
elif 9 <= n <= 11:
    print("Autumn")
elif n == 12 or 1 <= n <= 2:
    print("Winter")
else:
    print("Invalid")
