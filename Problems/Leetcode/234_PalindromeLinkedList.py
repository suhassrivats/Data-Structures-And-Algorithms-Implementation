# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity (Auxiliary): O(1)
        """
        fast = slow = head

        # Find the mid node. Fast pointer moves 2-steps and slow by 1-step
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half of the linkedlist
        slow = self.reverseList(slow)
        fast = head

        # Compare values of two halves (straight and reversed)
        while slow:
            if slow.val != fast.val:
                return False
            print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next

        return True

    def reverseList(self, head: ListNode) -> ListNode:
        """
        Visualize the output like this:
            Original:      1->2->3->4->None
            Output:  None<-1<-2<-3<-4
        """
        prev = None

        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev
