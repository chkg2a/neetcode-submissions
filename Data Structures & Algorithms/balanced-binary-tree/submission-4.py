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

        def dfs(root):
            if root == None:
                return 1

            left = dfs(root.left)
            right = dfs(root.right)
            print(left, right)

            return 1 + max(left,right)

        i = dfs(root.left)
        r = dfs(root.right)
        print(i,r)

        return True if abs(i - r) <= 1 else False