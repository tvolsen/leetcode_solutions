# 103. Binary Tree Zigzag Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        levels = {}
        q = deque([(root, 0)])
        while q:
            node, dist = q.popleft()
            if not node:
                continue
            if dist in levels:
                levels[dist].append(node.val)
            else:
                levels[dist] = [node.val]
            q.append((node.left, dist+1))
            q.append((node.right, dist+1))
        # -1**l is either -1 or 1, aka reverse on odd, keep the same on even numbers
        return [arr[::(-1)**(l)] for l,arr in levels.items()]
