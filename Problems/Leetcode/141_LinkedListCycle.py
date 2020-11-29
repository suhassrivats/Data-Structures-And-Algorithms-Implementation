# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        It is a safe choice to move the slow pointer one step at a time while
        moving the fast pointer two steps at a time. For each iteration, the
        fast pointer will move one extra step. If the length of the cycle is M,
        after M iterations, the fast pointer will definitely move one more
        cycle and catch up with the slow pointer.

        Time complexity: O(n)
        Space complexity (auxiliary): O(1)
        """

        slow, fast = head, head
        while fast and fast.next:
            # Move fast by 2-steps
            fast = fast.next.next
            # Move slow by 1-step
            slow = slow.next

            if slow == fast:
                return True

        return False
