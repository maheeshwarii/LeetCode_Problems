def longestBalanced(nums):
        n = len(nums)
        ans = 0
        for i in range(n):
           c = [0, 0]
           vis = set()
           for j in range(i, n):
               if nums[j] not in vis:
                   c[nums[j] & 1] +=1
                   vis.add(nums[j])
               if c[0] == c[1]:
                   ans = max(ans, j - i + 1)
        return ans

#main
nums = [2, 5, 4, 3]
print(longestBalanced(nums))