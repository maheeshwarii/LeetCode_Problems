def minPlatform(arr, dep):
    arr.sort()
    dep.sort()
    n = len(arr)
    pf_count = 0
    res = 0
    j = 0
    for i in range(n):
        while j < n and dep[j] < arr[i]:
            pf_count -= 1
            j += 1
        pf_count += 1
        res = max(res, pf_count)
    return res