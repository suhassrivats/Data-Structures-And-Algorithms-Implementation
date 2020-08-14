# Approach 1: Brute Force
class MapSum:
    """
    Complexity Analysis:
    Time Complexity: Every insert operation is O(1). Every sum operation is
    O(N * P)O(N∗P) where N is the number of items in the map, and P is the
    length of the input prefix.

    Space Complexity: The space used by map is linear in the size of all input
    key and val values combined.
    """

    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        for key, val in self.map.items():
            if key.startswith(prefix):
                total += val
        return total


# Approach 2: Prefix Hashmap
class MapSum:
    """
    Complexity Analysis:
    Time Complexity: Every insert operation is O(K^2), where K is the length of
     the key, as K strings are made of an average length of K. Every sum
     operation is O(1).

    Space Complexity: The space used by map and score is linear in the size of
    all input key and val values combined.
    """

    def __init__(self):
        self.map = {}
        self.score = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        prefix = ""
        for c in key:
            prefix += c
            self.score[prefix] = self.score.get(prefix, 0) + delta

    def sum(self, prefix: str) -> int:
        return self.score.get(prefix, 0)
