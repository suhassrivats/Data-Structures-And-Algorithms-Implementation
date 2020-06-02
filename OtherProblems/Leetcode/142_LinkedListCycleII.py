# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Time complexity: O(n) as the inner while-loop runs only once
        Space complexity (auxiliary): O(1)
        """
        slow = fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If slow==fast, a loop is detected. Now find start of the loop.
            if slow == fast:
                fast = head

                while fast is not slow:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None
