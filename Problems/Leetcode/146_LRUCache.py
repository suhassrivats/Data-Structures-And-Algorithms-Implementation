class DLLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):
    """
    Idea:
        - Use a doubly linked list
            - Add new items to tail. Therefore, most recently used (MRU) item is closer to the tail
            - Least recently used will be nearer to head
            - While adding items we need to make sure that we haven't exceeded the capacity of cache
        - If the get item is near the head or tail, then it is a O(1) operation. If not, it is going to be O(n). 
        - To avoid this, we can use a hashmap which will have key and value as the location of node. This way we can lookup the node in O(1) time and remove it. 
    """

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dic = dict()
        self.head = DLLNode(0, 0)
        self.tail = DLLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def put(self, key, value):
        # Set the value if the key is not present in the cache. If the cache
        # is at capacity remove the oldest item. We are adding new elements to
        # the tail of DLL. So by convention, element closer to tail is MRU
        # (Most Recently Used) and element closer to head is LRU
        if key in self.dic:
            self._remove(self.dic[key])
        # Add item closer to tail. Newly added item is MRU
        n = DLLNode(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next  # LRU node is always next to head
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
