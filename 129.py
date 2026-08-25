# 129. Sum Root to Leaf Numbers
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # return empty string for None nodes
            if not node:
                return ''
            # if no children, return str of node val
            if not node.left and not node.right:
                return str(node.val)
            # recurse on left and prepend curr node val
            left = dfs(node.left)
            left = [str(node.val) + s for s in left]
            # recurse on right and prepend curr node val
            right = dfs(node.right)
            right = [str(node.val) + s for s in right]
            # return left and right lists merged together
            return left + right
        paths = dfs(root)
        # convert str paths to ints and sum
        return sum([int(p) for p in paths])
