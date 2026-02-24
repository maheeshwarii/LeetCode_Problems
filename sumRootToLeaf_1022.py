class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root):
        def dfs(root, x):
            if root is None:
                return 0
            x = x << 1 | root.val
            if root.left == root.right:
                return x
            return dfs(root.left, x) + dfs(root.right, x)
        return dfs(root, 0)


root = TreeNode(1, TreeNode(0), TreeNode(1))   
sol = Solution()
print(sol.sumRootToLeaf(root))