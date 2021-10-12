"""Peter Rasmussen, Programming Assignment 1, sorts/merge_sort.py

The MergeSortPoints class sorts a list of x-y points and inherits from the MergeSort class.

"""

# Standard library imports
from copy import deepcopy
from typing import List

# Local imports
from merge_sort import MergeSort


class MergeSortPoints(MergeSort):
    def __init__(self, unsorted_li: List[dict]):
        super().__init__(unsorted_li)

    def two_way_merge(self, l1: list, l2: list):
        """
        Merge two sorted lists into one sorted list.
        :param l1: First list
        :param l2: Second list
        :return: Merged, sorted list
        """
        li_merge = []
        while l1 and l2:
            if l1[0]["distance"] < l2[0]["distance"]:
                li_merge.append(l1.pop(0))
            else:
                self.n_exchanges += 1
                li_merge.append(l2.pop(0))
            self.n_comparisons += 1

        return li_merge + l1 + l2
