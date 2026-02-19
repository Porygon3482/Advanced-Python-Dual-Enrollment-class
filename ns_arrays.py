"""
File: ns_arrays.py
Assignment: 4.5
Name: Neel Srivastava
Date: 18/2/26
Summary: This file defines an Array class that stores a fixed number of items and supports indexing, loops, len(), and printing.
added the __eq__ method so two Array objects can be compared with == by checking their sizes and items. I also added a clone()
method and tests to show that different arrays compare as False and a cloned array compares as True.

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.
"""

import random

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self._items[index] = newItem

    def __eq__(self, other):
        """Runs when an Array is the left operand of ==.
        Returns True if other is an Array, has the same logical size,
        and items at each logical position are equal. Otherwise returns False."""
        if not isinstance(other, Array):
            return False
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def clone(self):
        """Returns a deep copy of the Array."""
        newArray = Array(len(self))
        for i in range(len(self)):
            newArray[i] = self[i]
        return newArray


if __name__ == "__main__":
    capacity = 20
    size = capacity // 2
    my_array = Array(capacity)
    for i in range(size):
        # What method is called?
        my_array[i] = random.randint(1, capacity + 1)

    print("len = ", len(my_array))

    for item in my_array:
        print(item, end=" ")
    print("\n", "-" * 60)

    for i in range(size - 1, 0, -1):
        print(my_array[i], end = ", ")
    print()

    print(my_array)

    print("\n" + "=" * 60)
    print("== Equality Tests ==")

    # 2. Create 2 arrays containing random integers, each has 20 elements
    arr1 = Array(20)
    arr2 = Array(20)

    for i in range(20):
        arr1[i] = random.randint(1, 100)
        arr2[i] = random.randint(1, 100)

    # 2a. Compare 2 different arrays. The "==" comparison should be false.
    # Rare case: random fill could accidentally make them identical.
    # If that happens, force a difference in one position.
    if arr1 == arr2:
        arr2[0] = arr2[0] + 1

    print("\nArray 1:", arr1)
    print("Array 2:", arr2)
    print("arr1 == arr2 ?", arr1 == arr2)  # should be false

    # 2b. Clone one array and compare with the original. Should be true.
    arr3 = arr1.clone()
    print("\nCloned Array 3 (from Array 1):", arr3)
    print("arr1 == arr3 ?", arr1 == arr3)  # should be true
