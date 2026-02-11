def longestCommonPrefix(strs):
    for i in range(len(strs[0])):
        for j in strs[1:]:
            if len(j) <= i or j[i] != strs[0][i]:
                return j[:i]
    return strs[0]

#main
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))