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


# # solution example using new object attributes to reflect globals (self.ans, self.k)
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.ans = None
#         self.k = k
#         def dfs(node):
#             if not node:
#                 return
#             if self.ans is not None:
#                 return
#             dfs(node.left)
#             self.k -= 1
#             if self.k == 0:
#                 self.ans = node.val
#                 return
#             dfs(node.right)
#         dfs(root)
#         return self.ans

# # solution example using nonlocal to mimic globals
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         ans = None
#         def dfs(node):
#             nonlocal ans, k
#             if not node:
#                 return
#             if ans is not None:
#                 return
#             dfs(node.left)
#             k -= 1
#             if k == 0:
#                 ans = node.val
#                 return
#             dfs(node.right)
#         dfs(root)
#         return ans

