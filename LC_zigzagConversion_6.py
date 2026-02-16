from itertools import chain
def convert(s, numRows):
    if numRows == 1:
        return s
    g = [[] for _ in range(numRows)]
    a, b = 0, -1
    for i in s:
        g[a].append(i)
        if a == 0 or a == numRows - 1:
            b = -b
        a += b
    return ''.join(chain(*g))

#main
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))