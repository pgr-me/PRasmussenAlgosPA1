#!/usr/bin/env python3
"""Peter Rasmussen, Programming Assignment 1, sorts/heap_sort_points.py

The HeapSortPoints class sorts a list of x-y points.
"""

# Standard library imports
from typing import List, Union

# Local imports
from pa1.sorts.heap_sort import HeapSort


class HeapSortPoints(HeapSort):
    """Modification of Heap sort that sorts list of lists."""

    def __init__(self, li: List[List[Union[int, float]]]):
        """
        Constructor.
        :param li: Unsorted list
        """
        super().__init__(li)
        self.li = li

    def max_heapify(self, i: int):
        """
        Max heapify a subtree, rooted at index i, of lists.
        :param i: Index of root of subtree
        :return: Max-heapified tree
        """
        l = self.left(i)
        r = self.right(i)
        if (l <= self.heap_size - 1) and (self.li[l][-1] > self.li[i][-1]):
            largest = l
        else:
            largest = i
        if (r <= self.heap_size - 1) and (self.li[r][-1] > self.li[largest][-1]):
            largest = r
        if largest != i:
            self.li[i], self.li[largest] = self.li[largest], self.li[i]
            return self.max_heapify(largest)

    def sort(self) -> List[list]:
        """
        Sort a list of lists.
        :return: Sorted list
        """
        self.build_max_heap()
        for i in reversed(range(1, self.length)):
            self.li[0], self.li[i] = self.li[i], self.li[0]
            self.heap_size -= 1
            self.max_heapify(0)

        return self.li
