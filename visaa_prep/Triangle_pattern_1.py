n = int(input())
current_number = 1

for i in range(1, n + 1):
    row_numbers = [str(current_number + j) for j in range(i)]
    print(" ".join(row_numbers))
    current_number += i
