#57
def insert(intervals, newInterval):
    x = []
    i = 0
    n = len(intervals)
    while i < n and intervals[i][1] < newInterval[0]:
        x.append(intervals[i])
        i += 1
    
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    x.append(newInterval)
    while i < n:
        x.append(intervals[i])
        i += 1
    return x

#main
intervals = [[1,2], [3, 8], [6, 7], [8, 10], [12, 16]]
newInterval = [4,8]
print(insert(intervals, newInterval))