# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity (auxiliary): O(1)
            Since we are not creating any new nodes here, space complexity is
        O(1). we are just creating three new pointers overall irrespective of
        the input. So the space remains constant.
        """

        if head is None:
            return None

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even

        return head
