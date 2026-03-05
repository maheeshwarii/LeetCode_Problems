#55
def canJump(nums):
    n = len(nums)
    maxi = 0
    for i in range(n):
        if i > maxi:
            return False #it already crossed last index
        maxi = max(maxi, i + nums[i]) # the value and its index sum give no of jumps
    return True

#main
nums = [3, 2, 1, 0, 4]
print(canJump(nums))