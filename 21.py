# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # this handles edge cases on empty inputs
        dummy = ListNode(0, None)
        # use curr to build up dummy
        curr = dummy
        # while both pointers have not reached the end
        while list1 and list2:
            # add the smaller value to curr
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            # advance curr
            curr = curr.next
        # point the end of curr to the pointer on whichever list is not yet finished
        curr.next = list1 or list2
        # return actual start of dummy
        return dummy.next
