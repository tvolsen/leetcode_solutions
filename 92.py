# 92. Reverse Linked List II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # edge case handling
        if not head or left == right:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        # iterate prev until we are just before left
        for _ in range(left-1):
            prev = prev.next
        # make curr the first element to be reversed
        curr = prev.next
        # reverse all elements between left and right
        for _ in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        # return head
        return dummy.next
