# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter
            
            if node is None:
                return 0

            L = dfs(node.left)
            R = dfs(node.right)

            diameter = max(diameter, L + R)

            return 1 + max(L, R)

        dfs(root)
        return diameter

        