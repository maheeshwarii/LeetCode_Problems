#435
def eraseOverlapInterval(intervals):
    ends = []
    for s, e in intervals:
        ends.append((e, s))
    ends.sort()
    c = 0
    le = ends[0][0]
    for e, s in ends[1:]:
        if s < le:
            c += 1
        else:
            le = e
    return c

#main
intervals = [ (1, 2), (2, 3), (1, 3), (3, 4) ]
print(eraseOverlapInterval(intervals))