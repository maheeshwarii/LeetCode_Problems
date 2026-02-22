def binaryGap(n):
    ans = 0
    prev, curr = float('inf'), 0
    while n:
        if n & 1:
            ans = max(ans, curr - prev)
            prev = curr
        curr += 1
        n >>= 1
    return ans

#main
n = 9
print(binaryGap(n))