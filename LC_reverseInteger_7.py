def reverse(x):
    ans = 0
    mn = - (2**31)
    mx = (2**31) - 1
    while x:
        if ans < mn // 10 + 1 or ans > mx // 10:
            return 0
        y = x % 10
        if x < 0 and y > 0:
            y -= 10
        ans = ans * 10 + y
        x = (x - y) // 10
    return ans

#main
x = 123
print(reverse(x))