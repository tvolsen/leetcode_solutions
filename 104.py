# 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        # base case
        if not root:
            return 0
        # add root and depth 1 to q
        q = deque([(root, 1)])
        ans = 1
        # continue until all nodes have been visited
        while q:
            # pop first entered node and depth
            node, depth = q.popleft()
            # if bottom is reached, continue
            if not node:
                continue
            # update ans
            ans = max(ans, depth)
            # add left and right with depth+1 to q
            q.append((node.left, depth+1))
            q.append((node.right, depth+1))
        return ans
