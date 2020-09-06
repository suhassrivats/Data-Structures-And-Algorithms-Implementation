# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        Time complexity:
            The time complexity of our algorithm will be O(N) where ‘N’ is the
        total number of nodes in the LinkedList.

        Space complexity:
            We only used constant space, therefore, the space complexity of our
        algorithm is O(1).
        """
        if m == n:
            return head

        # get the p-1 node
        current, previous = head, None
        i = 0
        while current and i < m-1:
            previous = current
            current = current.next
            i += 1
        last_node_of_first_sublist = previous

        # after reversing current will become the last node of sublist
        last_node_of_reversed_sublist = current

        # reverse q-p+1 nodes
        next_node = None
        i = 0
        while current and i < n-m+1:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            i += 1

        # connect with the first part
        if last_node_of_first_sublist:
            # previous is the first node of reversed sublist
            last_node_of_first_sublist.next = previous
        else:
            head = previous

        # connect with the last part
        last_node_of_reversed_sublist.next = current

        return head
