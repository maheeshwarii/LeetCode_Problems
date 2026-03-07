#875
from math import ceil
def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    ans = right
    while left <= right:
        mid = (left + right)//2
        hours = 0
        for p in piles:
            hours += ceil(p/mid)
        if hours <= h:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

#main
piles = [14, 20, 19, 32, 17, 18]
h = 12
print(minEatingSpeed(piles, h))