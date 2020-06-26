# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Time complexity : O(max(m, n)). Assume that mm and nn represents the
        length of l1l1 and l2l2 respectively, the algorithm above iterates at
        most max(m, n) times.

        Space complexity : O(max(m,n)). The length of the new list is at most
        max(m,n) + 1.
        """

        result = n = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            n.next = ListNode(val)
            n = n.next

        return result.next
