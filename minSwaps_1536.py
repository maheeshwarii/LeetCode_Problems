def minSwaps(grid):
    n = len(grid)
    pos = []
    for row in grid:
        j = n - 1
        while j >= 0 and row[j] == 0:
            j -= 1
        pos.append(j)  
    ans = 0
    for i in range(n):
        need = i
        k = -1
        for j in range(i, n):
            if pos[j] <= need:
                ans += j - i  
                k = j
                break
        if k == -1:
            return -1  # impossible
        while k > i:
            pos[k], pos[k-1] = pos[k-1], pos[k]
            k -= 1
    return ans

#main
grid = [[0,0,1],[1,1,0],[1,0,0]]
print(minSwaps(grid))