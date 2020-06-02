# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity (Auxiliary): O(1)

        Edge cases:
        - The linked list is empty, i.e. the head node is None.
        - Multiple nodes with the target value in a row.
        - The head node has the target value.
        - The head node, and any number of nodes immediately after it have the
        target value.
        - All of the nodes have the target value.
        - The last node has the target value.
        """

        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head

        while current_node.next is not None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return dummy_head.next
