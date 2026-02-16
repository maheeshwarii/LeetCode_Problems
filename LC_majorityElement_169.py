def majorityElement(nums):
    a = b = 0
    for i in nums:
        if a == 0:
            b, a = i, 1
        else:
            a += 1 if b == i else -1
    return b

#main
nums = [3, 2, 3]
print(majorityElement(nums))