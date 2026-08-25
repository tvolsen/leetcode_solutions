# 236. Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            # if p is found, return it
            if node.val == p.val:
                return node
            # if q is found, return it
            if node.val == q.val:
                return node
            # search left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            # if both subtrees returned a node, curr node is LCA
            if left and right:
                return node
            # otherwise send up which one was found
            else:
                return left or right
        return dfs(root)      
            
