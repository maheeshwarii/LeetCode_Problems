def findKthBit(n, k):
    def dfs(n, k):
        if n == 1:
            return "0"
        length = (1 << n) - 1
        mid = (length // 2) + 1
        if k == mid:
            return "1"
        elif k < mid:
            return dfs(n-1, k)
        else:
            mirrored = length - k + 1
            bit = dfs(n-1, mirrored)
            return "1" if bit == "0" else "0"
    return dfs(n, k)

#main
n = 4
k = 3
print(findKthBit(n, k))