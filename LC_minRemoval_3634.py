def minRemoval(nums, k):
    nums.sort()
    n = len(nums)
    l = 0
    max_keep = 0
    for i in range(n):
        while nums[i] > k * nums[l]:
            l += 1
        max_keep = max(max_keep, i - l + 1)
    return n - max_keep

#main
nums = [1, 2, 6, 9]
k = 3
print(minRemoval(nums, k))