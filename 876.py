# 876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # point fast and slow to head
        fast = head
        slow = head
        # move fast twice the speed of slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # this means slow will be the mid point of the list
        return slow
