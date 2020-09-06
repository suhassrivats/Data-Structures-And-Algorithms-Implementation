# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Visualize the output like this:
            Original:      1->2->3->4->None
            Output:  None<-1<-2<-3<-4
        """
        previous, next_node = None, None
        current = head
        while current:
            next_node = current.next  # temporarily store the next pointer
            current.next = previous  # reverse the current node
            previous = current  # before we move to the next node, point previous to the current node
            current = next_node  # move on the next node
        return previous
