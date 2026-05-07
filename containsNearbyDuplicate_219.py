def containsNearbyduplicate(nums, k):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen and i - seen[nums[i]] <= k:
            return True
        seen[nums[i]]= i
    return False

#main
nums = [1, 2, 3, 1]
k = 3
print(containsNearbyduplicate(nums, k))