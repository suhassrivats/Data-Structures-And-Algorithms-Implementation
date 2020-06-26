# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Time complexity: O(L)
            The algorithm makes one traversal of the list of LL nodes.
        Therefore time complexity is O(L).

        Space complexity: O(1)
            We only used constant extra space.
        """

        dummy = ListNode(0)
        slow = fast = dummy
        dummy.next = head

        # Advances first pointer so that the gap between first and second is n
        # nodes apart
        for _ in range(n):
            fast = fast.next

        # Move first to the end, maintaining the gap
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        # Removing a node
        slow.next = slow.next.next

        return dummy.next
