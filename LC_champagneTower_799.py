def champagneTower(poured, query_row, query_glass):
    f = [poured]
    for i in range(1, query_row + 1):
        g = [0] * (i + 1)
        for j, v in enumerate(f):
            if v > 1:
                half = (v - 1) / 2
                g[j] += half
                g[j + 1] += half
        f = g
    return min(1, f[query_glass])

#main
poured = 2
query_row = 1
query_glass = 1
print(champagneTower(poured, query_row, query_glass))