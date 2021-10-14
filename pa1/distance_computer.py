#!/usr/bin/env python3
"""Peter Rasmussen, Programming Assignment 1, distance_computer.py

The DistanceComputer computes distances among an array of X-Y points.

"""


# Standard library imports
from typing import Union, List


class DistanceComputer:
    """Computes the distances among an array of X-Y points."""

    def __init__(self, raw_points: List[list]):
        """
        Initialize raw points, distances list, and computation counter.
        :param raw_points: List of X-Y pairs

        Example distances object: [{'point1': (0, 0), 'point2': (0, 1), 'distance': 1.0}, ...]
        """
        self.raw_points = raw_points
        self.distances: Union[List[dict], None] = None
        self.n_dist_comps: int = 0

    def compute_distances(self) -> List[List[Union[int, float]]]:
        """
        Compute distances among coordinate pairs.
        :return: Distance among coordinate pairs.
        """
        self.distances = []
        for i in range(len(self.raw_points)):
            for j in range(i + 1, len(self.raw_points)):
                distance = self.compute_distance(self.raw_points[i], self.raw_points[j])
                li = [self.raw_points[i], self.raw_points[j], distance]
                self.distances.append(li)
                self.n_dist_comps += 1
        return self.distances

    @staticmethod
    def compute_distance(p1: List[int], p2: List[int]) -> float:
        """
        Compute distance between two coordinates.
        :param p1: Point 1 coordinates
        :param p2: Point 2 coordinates
        :return: Distance between Points 1 and 2
        """
        x1, y1 = p1
        x2, y2 = p2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
