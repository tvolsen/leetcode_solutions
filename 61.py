# 61. Rotate List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base case
        if not head:
            return head

        # calculate the length of list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # each k iterations is a cycle, so we need to mod by length to save compute
        k = k % length
        if k == 0:
            return head

        curr = head
        # travel until just before the split point
        for i in range(length-k-1):
            curr = curr.next

        # create the tail of the original list
        tail = curr.next
        # break off tail
        curr.next = None

        # append head to tail (tail -> head)
        dummy = ListNode()
        dummy.next = tail
        curr = dummy
        while curr.next:
            curr = curr.next
        curr.next = head
        # return tail -> head as a list
        return dummy.next
    
