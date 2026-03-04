#128
#Time complexity: O(Nlogn)

def longestConsecutive(nums):
    '''if not nums:
        return 0
    nums.sort()
    curr = 1
    max_len = 1
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]: #Ignore duplicates
            continue
        elif nums[i - 1] + 1 == nums[i]: #Search for sequence
            curr += 1
            max_len = max(curr, max_len)
        else:                           #
            curr = 1
    return max_len'''

    max_len = 0
    curr = 0
    nums_set = set(nums)
    for num in nums_set:
        if num - 1 not in nums_set:
            curr = num
            l = 1
            while curr + 1 in nums_set:
                curr += 1
                l += 1
            max_len = max(max_len, l)
    return max_len



nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))