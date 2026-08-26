# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        failed = True

        def dfs(root):
            if root == None:
                return 1

            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                failed = True
            return 1 + max(left,right)

        i = dfs(root.left)
        r = dfs(root.right)
        print(i,r)

        if abs(i-r) <= 1 and failed == True:
            return True
        else:
            return False