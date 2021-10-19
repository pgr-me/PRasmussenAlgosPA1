#!/usr/bin/env python3
"""Peter Rasmussen, Programming Assignment 1, sorts/heap_sort.py

This module implements a recursive version of the heap sort.

I based this class on the heap sort pseudo code provided in
Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. 2009. Introduction to
Algorithms, Third Edition (3rd. ed.). The MIT Press.
"""

# Standard library imports
from typing import List


class HeapSort:
    """Recursive implementation of heap sort based on Chapter 6 of CLRS."""

    def __init__(self, li):
        """
        Constructor.
        :param: List of sortable items
        """
        self.li = li
        self.heap_size = len(li)
        self.length = len(li)
        self.n_heapifies = 0

    def build_max_heap(self):
        """
        Build a max heap in-place.
        """
        for i in reversed(range(len(self.li) // 2)):
            self.n_heapifies += 1
            self.max_heapify(i)

    def max_heapify(self, i: int):
        """
        Max heapify a subtree rooted at index i.
        :param i: Index of root of subtree
        """
        left = self.left(i)
        right = self.right(i)
        if (left <= self.heap_size - 1) and (self.li[left] > self.li[i]):
            largest = left
        else:
            largest = i
        if (right <= self.heap_size - 1) and (self.li[right] > self.li[largest]):
            largest = right
        if largest != i:
            self.li[i], self.li[largest] = self.li[largest], self.li[i]
            self.n_heapifies += 1
            return self.max_heapify(largest)

    def sort(self) -> List[list]:
        """
        Heap-sort list.
        :return: Sorted list
        """
        self.build_max_heap()
        for i in reversed(range(1, self.length)):
            self.li[0], self.li[i] = self.li[i], self.li[0]
            self.heap_size -= 1
            self.n_heapifies += 1
            self.max_heapify(0)

        return self.li

    @staticmethod
    def left(i: int) -> int:
        """
        Return left child of parent node.
        :param i: Parent node index
        :return: Left child
        """
        return 2 * i

    @staticmethod
    def right(i: int) -> int:
        """
        Return right child of parent node.
        :param i: Parent node index
        :return: Right child
        """
        return 2 * i + 1
