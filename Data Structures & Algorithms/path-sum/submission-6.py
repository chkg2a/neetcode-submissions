# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.sol = False
        def dfs(node, val):
            if node.right is None and node.left is None and val + node.val == targetSum:
                self.sol=True
                return
            
            if node.right:
                dfs(node.right,val + node.val)
            if node.left:
                dfs(node.left,val + node.val)
        if root:
            dfs(root,0)
        return self.sol