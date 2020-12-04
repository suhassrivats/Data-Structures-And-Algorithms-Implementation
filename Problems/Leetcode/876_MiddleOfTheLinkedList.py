# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        Time Complexituy: O(N) where N is the number of nodes in a given list
        Space Complexity: O(N), space used by A. We store all given nodes to A
        """
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A)//2]


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
