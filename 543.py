# 543. Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # if you hit a null child, return 0s
            if not node:
                return 0, 0
            # return the largest ans and longest path from left and right
            left_ans, left_path = dfs(node.left)
            right_ans, right_path = dfs(node.right)
            # update ans to be the diameter centered at the curr node
            # or the ans from left or right 
            ans = max(left_ans, right_ans, left_path+right_path)
            # add 1 to the longer path, this 1 is the edge between curr and it's parent
            path = max(left_path, right_path) + 1
            return ans, path
        return dfs(root)[0]
