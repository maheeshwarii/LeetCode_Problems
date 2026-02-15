def version(version1, version2):
    i = j = 0
    m, n = len(version1), len(version2)
    while i < m or j < n:
        a = b = 0
        while i < m and version1[i] != '.':
            a = a * 10 + int(version1[i])
            i += 1
        while j < n and version2[j] != '.':
            b = b * 10 + int(version2[j])
            j += 1
        if a != b:
            if a < b: return -1
            else: return 1
        i += 1
        j += 1
    return 0

#main
version1 = "1.2"
version2 = "1.10"
print(version(version1, version2))