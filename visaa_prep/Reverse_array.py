def reverse_array(n, array):
    array.reverse()
    print(" ".join(map(str, array)))

n = int(input())
array = list(map(int, input().split()))

reverse_array(n, array)
