# 199. Binary Tree Right Side View
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        ans = []
        q = deque([(root, 0)])
        while q:
            node, dist = q.popleft()
            if node.left:
                q.append((node.left, dist+1))
            if node.right:
                q.append((node.right, dist+1))
            if q:
                new_dist = q[0][1]
                if new_dist > dist:
                    ans.append(node.val)
        ans.append(node.val)
        return ans
