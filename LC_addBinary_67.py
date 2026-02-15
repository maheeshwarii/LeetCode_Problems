def addBinary(a, b):
    ans = []
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        carry, v = divmod(carry, 2)
        ans.append(str(v))
    return "".join(ans[::-1])

#main
a = "1010"
b = "1011"
print(addBinary(a, b))