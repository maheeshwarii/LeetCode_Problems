def nextGreaterElement(nums1, nums2):
    stack = []
    NGE = {}
    for i in nums2:
        while stack and stack[-1]<i:
            NGE[stack.pop()] = i
        stack.append(i)
    while stack: 
        NGE[stack.pop()] = -1
    result = []
    for i in nums1:
        result.append(NGE[i])
    return result

#main
nums2 = list(map(int,input("Enter list elements:").split()))
nums1 = list(map(int, input("Enter subset liste elements:").split()))
print(nextGreaterElement(nums1, nums2))