def reduce_string(S):
    result = ""
    count = 1
    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            count += 1
        else:
            result += S[i - 1] + str(count)
            count = 1
    result += S[-1] + str(count)
    return result

inputStr = input()
print(reduce_string(inputStr))
