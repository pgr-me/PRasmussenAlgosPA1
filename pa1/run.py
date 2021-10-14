"""Peter Rasmussen, Programming Assignment 1, run.py

The run function reads a file of one or more n-m combinations, produces a random
uniform distribution of 2D points, computes the distances between each pair of points, sorts the
point pairs in ascending order by distance, and saves statistical and closest pairs outputs to the
selected destination directory.

"""

# standard library imports
import csv
import json
import logging
import os
from pathlib import Path
from typing import List, Union

# local imports
from pa1.datamaker import DataMaker
from pa1.distance_computer import DistanceComputer
from pa1.file_io import read_input_params, write_stats_outputs, write_closest_pairs_outputs
from pa1.sorts import HeapSortPoints


def run(
        src: Path,
        dst_dir: Path,
        seed: int,
        file_header: str):
    """
    Symbolically combine polynomials and then evaluate for various evaluation sets.
    :param src: Input CSV path
    :param dst_dir: Output directory
    :param seed: Random number seed
    :param file_header: Header to add to top of output CSV
    """
    dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
    log_path = dir_path / "pa1.log"
    logging.basicConfig(filename=log_path, level=logging.DEBUG)

    logging.debug("Read data and check, among other things, that m <= n")
    input_params: List[List[Union[int, float]]] = read_input_params(src)

    logging.debug("Iterate over each n, m pair")
    stats_output = [["n", "m", "n_dist_comps", "n_heapifies", "total_ops"]]
    closest_pairs_output = []
    for row in input_params:
        n, m = row
        print(f"n={n}, m={m}")

        # Generate sequence of randomly dispersed points
        data_maker = DataMaker(n, seed=seed)
        points: List[List[Union[int, float]]] = data_maker.make_data()

        # Compute distances among points
        distance_computer = DistanceComputer(points)
        points = distance_computer.compute_distances()

        # Sort points
        heap_sort_points = HeapSortPoints(points)
        points = heap_sort_points.sort()

        # Select nearest m pairs
        m_closest_pairs = points[:m]

        # Compute total number of operations
        total_ops = distance_computer.n_dist_comps + heap_sort_points.n_heapifies

        # Organize outputs
        di = {"n": n, "m": m, "m_closest_pairs": m_closest_pairs, "all_points": data_maker.points}
        closest_pairs_output.append(di)

        # Append current run to output list of runs
        li = [n, m, distance_computer.n_dist_comps, heap_sort_points.n_heapifies, total_ops]
        stats_output.append(li)

    logging.debug("Write performance outputs to CSV.")
    stats_dst = dst_dir / f"{src.stem}_output.csv"
    write_stats_outputs(stats_dst, file_header, stats_output)

    logging.debug("Write set of m closest pairs for given n to JSON.")
    closest_pairs_dst = dst_dir / f"{src.stem}_output.json"
    write_closest_pairs_outputs(closest_pairs_dst, closest_pairs_output)

    logging.debug("Finish.")
