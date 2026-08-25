# 230. Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, k):
            if not node:
                return k, None
            k, found = dfs(node.left, k)
            if found is not None:
                return k, found
            k -= 1
            if k == 0:
                return k, node.val
            return dfs(node.right, k)
        return dfs(root, k)[1]
