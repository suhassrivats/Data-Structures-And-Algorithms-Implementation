# Implementation of Dynamic Array in Python

import ctypes


class DynamicArray(object):
    """A dynamic array similar to Python List"""

    def __init__(self):
        # Count the number of elements
        self.n = 0
        # Array capacity of atleast 1
        self.capacity = 1
        # Make an array of size n
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """Return the number of items in a list.
        While you can call these methods directly
        ([10, 20].__len__() for example), the presence of the underscores
        is a hint that these methods are intended to be invoked indirectly
        (len([10, 20]) for example). Most python operators have an associated
        "magic" method (for example, a[x] is the usual way of invoking
        a.__getitem__(x)).
        """
        return self.n

    def __getitem__(self, k):
        """Return the element at index k.
        For example, a[x] is the usual way of invoking a.__getitem__(x))
        """
        if (k < 0) and (k > self.n):
            return IndexError("K is out of bounds")
        else:
            # Retrieve an element from array at position k
            print("Get item is:", self.A[k])
            return self.A[k]

    def append(self, ele):
        """Add element to end of the array"""
        
        # If array is full, then resize it to double the capacity
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._resize(2 * self.capacity)
        
        # Add an element to the end of an array
        self.A[self.n] = ele  
        # Increment n by 1 to keep count of the elements
        self.n += 1

    def _resize(self, new_cap):
        """Resize the array to a larger capacity.
        _single_leading_underscore: weak "internal use" indicator.
        E.g. from M import * does not import objects whose name starts
        with an underscore.
        """

        # Make a new array with larger capacity
        B = self.make_array(new_cap)

        # Copy all elements of small arr to big arr
        for k in range(self.n):
            B[k] = self.A[k]

        # Assign the new array to old one
        self.A = B

        # Update capacity with new capacity
        self.capacity = new_cap

    def make_array(self, new_cap):
        """Returns a new array with new capacity"""
        return (new_cap * ctypes.py_object)()


# Instantiate
arr = DynamicArray()
# Append new element
arr.append(1)
len(arr)
arr.append(1)
# # Append new element
arr.append(2)
# # Check length
len(arr)
arr[2]
