def findMaxForm(strs, m, n):
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in strs:
        z = i.count('0')
        o = i.count('1')
        for j in range(m, z-1, -1):
            for k in range(n, o-1,-1):
                dp[j][k] = max( dp[j][k], dp[j-z][k-o]+1)
    return dp[m][n]
#main
raw_strs = input("Enter the string:")
strs = [s.strip() for s in raw_strs.split(',')]
m = int(input("Enter max zeroes:"))
n = int(input("Enter max ones:"))
result = findMaxForm(strs, m, n)
print(f"Maximum number of strings you can pick: {result}")