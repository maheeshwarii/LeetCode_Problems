def strStr(haystack, needle):
    m, n = len(haystack), len(needle)
    for i in range( m - n + 1):
        if haystack[i : i + m] == needle:
            return i
    return -1

#main
haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))