# 2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        # start adding lists together until one exhausts
        while l1 and l2:
            value = l1.val + l2.val + carry
            if value >= 10:
                value -= 10
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(value, None)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        # finish off l1
        while l1:
            value = l1.val + carry
            if value >= 10:
                value -= 10
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(value, None)
            curr = curr.next
            l1 = l1.next

        # finish off l2
        while l2:
            value = l2.val + carry
            if value >= 10:
                value -= 10
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(value, None)
            curr = curr.next
            l2 = l2.next
        # if carry, add one extra node with value 1
        if carry:
            curr.next = ListNode(carry, None)
        return dummy.next
