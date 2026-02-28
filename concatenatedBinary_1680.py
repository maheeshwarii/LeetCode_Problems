def concatenatedBinary(n):
    res = 0
    for i in range(1, n + 1):
        length = i.bit_length()
        res = (res << length) + i
        res %= ((10**9) + 7)
    return res

#main
n = 3
print(concatenatedBinary(n))