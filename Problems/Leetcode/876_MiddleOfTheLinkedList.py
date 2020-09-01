# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        Time complexity:
            The above algorithm will have a time complexity of O(N) where ‘N’
        is the number of nodes in the LinkedList.

        Space complexity:
            The algorithm runs in constant space O(1).
        """

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
