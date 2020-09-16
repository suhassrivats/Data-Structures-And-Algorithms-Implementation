import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Note:
        - "Tuple comparison breaks for (priority, task) pairs if the priorities are
        equal and the tasks do not have a default comparison order."
        - So I added an arbitrary dummy element in between node.val and node.
        - Python3 solution which avoids "TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'."

        Time complexity:
            Since we’ll be going through all the elements of all arrays and
        will be removing/adding one element to the heap in each step, the time
        complexity of the above algorithm will be O(N*logK), where ‘N’ is the
        total number of elements in all the ‘K’ input arrays.

        Space complexity #
            The space complexity will be O(K) because, at any time, our min-heap
        will be storing one number from all the ‘K’ input arrays.
        """

        min_heap, count = [], 0
        cur = dummy = ListNode(-1)

        # put the root of each list in min_heap
        for head in lists:
            if head is not None:
                heapq.heappush(min_heap, (head.val, count, head))
                count += 1

        # take the smallest(top) element form the min-heap and add it to the
        # result if the top element has a next element add it to the heap
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            cur.next = node
            if node.next:
                heapq.heappush(min_heap, (node.next.val, count, node.next))
                count += 1
            cur = cur.next

        return dummy.next
