# 109. Convert Sorted List to Binary Search Tree
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        # find root
        def find_root(head_):
            if not head_:
                return None
            if not head_.next:
                return TreeNode(head_.val, None, None)
            slow = head_
            fast = head_
            prev = None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            root = slow.val
            right = slow.next
            prev.next = None
            left = head_
            return TreeNode(root, find_root(left), find_root(right))
        return find_root(head)
