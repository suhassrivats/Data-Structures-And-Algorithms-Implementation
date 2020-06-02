# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        """
        Time Complexity: O(n + m)
        Space Complexity:
            Input Space: O(n + m)
            Auxiliary Space: O(1)
            Total: Input + Auxiliary => O(n + m + 1) => O(n + m)

        Idea:
        1. Calculate the length of both linkedlists
        2. Find the absolute diff of their lengths
        3. Move diff number of nodes in longer linked list
        4. Move both linked list simultaneously until curA==curB
        """

        lenA, lenB = 0, 0
        curA, curB = headA, headB

        # find the length of two linkedlists
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next

        curA, curB = headA, headB
        diff = abs(lenA - lenB)

        # make starting points of longer linkedlist same as the shorter one
        for i in range(diff):
            if lenA >= lenB:
                curA = curA.next
            else:
                curB = curB.next

        # Now that both starting points are equal, increment both
        # simultaneously
        while curA != curB:
            curA, curB = curA.next, curB.next

        # If both are equal, then there is an intersection point. Therefore,
        # we can either return curA or curB. If linkedlist search is exhaused
        # curA and curB will point to None
        return curA
