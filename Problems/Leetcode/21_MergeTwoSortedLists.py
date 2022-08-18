# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Time Complexity: O(l1 + l2)
        Space Complexity (Auxiliary): O(1)

        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        # Make sure that sorting_ptr points to the beginning of linked list
        if l1 and l2:
            if l1.val <= l2.val:
                sorting_ptr = l1  # s points to head node of list1
                l1 = sorting_ptr.next  # list1 pointer points to next node
            else:
                sorting_ptr = l2
                l2 = sorting_ptr.next

        # Pointer to the beginning of a new_sorted linked list
        new_head = sorting_ptr

        # Move the sorting_ptr to the next lowest value
        while l1 and l2:
            if l1.val <= l2.val:
                sorting_ptr.next = l1
                sorting_ptr = l1
                l1 = sorting_ptr.next
            else:
                sorting_ptr.next = l2
                sorting_ptr = l2
                l2 = sorting_ptr.next

        if l1 is None:
            sorting_ptr.next = l2
        if l2 is None:
            sorting_ptr.next = l1

        return new_head
