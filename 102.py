# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # import deque
        from collections import deque
        # create the q with root and dist=0
        q = deque([(root, 0)])
        # create a tracker of all levels seen
        levels = {}
        # while there are nodes to process, keep going
        while q:
            # pop the earliest seen node
            node, dist = q.popleft()
            # if we have hit the bottom of the tree, continue
            if not node:
                continue
            # append to or create a new list at level dist
            if dist in levels:
                levels[dist].append(node.val)
            else:
                levels[dist] = [node.val]
            # add the left and right children to q
            q.append((node.left, dist+1))
            q.append((node.right, dist+1))
        # return the list of nodes at each level
        return [l for l in levels.values()]
