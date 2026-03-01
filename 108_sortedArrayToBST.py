class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):   
        def bst(left, right):
            if left > right:
                return None
            mid = (left + right) >> 1
            return TreeNode( nums[mid], bst(left, mid - 1), bst(mid + 1, right) )
        return bst(0, len(nums) - 1)

# main
nums = [-10, -3, 0, 5, 9]
s = Solution()
root = s.sortedArrayToBST(nums)   
print(root)