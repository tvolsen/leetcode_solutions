# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # original head should point to None when reversed
        prev = None
        # start at head
        curr = head
        # iterate through
        while curr:
            # store the next node in the list
            temp = curr.next
            # reverse the next link
            curr.next = prev
            # move prev to curr node
