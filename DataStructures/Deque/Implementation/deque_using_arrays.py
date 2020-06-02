# Implementation of deque using dynamic arrays/lists


class Deque:
    """
    In this implementation adding and removing items from the rear is O(1)
    whereas adding and removing from the front is O(n). This is to be expected
    given the common operations that appear for adding and removing items.
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_rear(self, item):
        self.items.append(item)

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_rear(self):
        return self.items.pop()

    def remove_front(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    d = Deque()
    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)
    print(d.size())
    print(d.is_empty())
    d.add_rear(8.4)
    print(d.remove_rear())
    print(d.remove_front())
