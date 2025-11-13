def maxOperations(s):
    ones = ans = 0
    for i, c in enumerate(s):
        if c=='1': ones += 1
        elif i>0 and s[i-1]== '1': ans += ones
    return ans
#main
s = input("Enter a binary string: ")
print(maxOperations(s))