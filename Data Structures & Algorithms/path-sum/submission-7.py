# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        def dfs(node,currSum):
            currSum += node.val
            if node.left is None and node.right is None:
                return currSum == targetSum
            left = False
            right = False
            if node.left:
                left = dfs(node.left, currSum)

            if node.right:
                right = dfs(node.right, currSum)
            return left or right
        return dfs(root,0)