# 107. Binary Tree Level Order Traversal II
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        ans = []
        q = deque([(root, 0)])
        curr = []
        while q:
            node, dist = q.popleft()
            curr.append(node.val)
            if node.left:
                q.append((node.left, dist+1))
            if node.right:
                q.append((node.right, dist+1))
            if not q:
                ans.append(curr[:])
            if q and q[0][-1] > dist:
                ans.append(curr[:])
                curr = []
        return ans[::-1]
