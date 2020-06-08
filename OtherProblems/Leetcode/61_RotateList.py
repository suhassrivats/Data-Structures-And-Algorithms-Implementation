# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if head is None:
            return None

        curr = head
        length = 1

        # Find the length of given linked list
        while curr.next:
            curr = curr.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length

        # Point the last element to the head. Making it a circular. At this
        # time curr is pointing to the last element.
        curr.next = head

        # Traverse list to get to the node just before ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)

        temp = head
        for _ in range(length-k-1):
            temp = temp.next

        # Get next node from tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        result = temp.next
        temp.next = None

        return result
