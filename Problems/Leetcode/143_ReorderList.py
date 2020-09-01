# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.

        Time Complexity:
            The above algorithm will have a time complexity of O(N) where ‘N’
        is the number of nodes in the LinkedList.

        Space Complexity:
            The algorithm runs in constant space O(1).
        """

        if head is None or head.next is None:
            return None

        # find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head_second_half = self.reverse(slow)
        head_first_half = head

        # rearrange to produce output in expected order
        while head_first_half and head_second_half:
            temp = head_first_half.next
            head_first_half.next = head_second_half
            head_first_half = temp

            temp = head_second_half.next
            head_second_half.next = head_first_half
            head_second_half = temp

        # Set last node to None
        if head_first_half:
            head_first_half.next = None

    def reverse(self, head):
        prev = None

        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev
