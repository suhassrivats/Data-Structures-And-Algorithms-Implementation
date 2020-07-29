# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Iteratively
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        second = head.next
        pre = ListNode(0)

        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            pre.next = tmp
            head = head.next
            pre = tmp.next

        return second


# Recursively
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head

        return second
