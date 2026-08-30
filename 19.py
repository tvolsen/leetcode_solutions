# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node before head
        dummy = ListNode(0, head)
        # start the lagging pointer at the dummy
        # this is because we want slow just
        # before the node to be deleted
        slow = dummy
        # point the fast pointer at the head
        fast = head
        # create a gap of distance n between the pointers
        for i in range(n):
            fast = fast.next
        # iterate until the fast pointer reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        # skip over the deletion node
        slow.next = slow.next.next
        # return the start of the list
        return dummy.next
