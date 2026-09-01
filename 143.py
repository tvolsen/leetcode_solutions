# 143. Reorder List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid point
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse tail
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge
        l1 = head
        l2 = prev
        while l1 and l2:
            # save the next pointers
            temp1 = l1.next
            temp2 = l2.next
            # weave the lists together
            l1.next = l2
            l2.next = temp1
            # advance pointers
            l1 = temp1
            l2 = temp2
