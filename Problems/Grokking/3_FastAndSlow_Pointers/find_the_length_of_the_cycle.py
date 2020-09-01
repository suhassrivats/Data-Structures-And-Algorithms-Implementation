class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_length(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return calculate_cycle_length(slow)
    return 0


def calculate_cycle_length(slow):
    cycle_length = 0
    current = slow
    while current:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length
