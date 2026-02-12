from collections import Counter
def longestBalanced(s):
    ans = 0
    for i in range(len(s)):
        mx = d = 0
        c = Counter()
        for j in range(i, len(s)):
            c[s[j]] += 1
            mx = max(mx, c[s[j]])
            if c[s[j]] == 1:
                d += 1
            if mx* d == j - i + 1:
                ans = max(ans, j - i + 1)
    return ans

#main
s = "abbac"
print(longestBalanced(s))