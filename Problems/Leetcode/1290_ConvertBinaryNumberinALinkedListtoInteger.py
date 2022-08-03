# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        T: O(N)
        S: O(1)
        """
        result = head.val
        while head.next:
            result = result*2 + head.next.val
            head = head.next
        return result
