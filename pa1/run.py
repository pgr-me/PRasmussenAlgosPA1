"""Peter Rasmussen, Lab 4, run.py

This module processes a reads a file or directory of files containing integers, executes five
recursive sorting algorithms, and an output CSV for each input file.

"""

# standard library imports
import csv
from copy import deepcopy
from pathlib import Path
from typing import List

# local imports
from pa1.datamaker import DataMaker
from pa1.distance_computer import DistanceComputer
from pa1.file_io import read_input_params
from pa1.sorts.merge_sort_points import MergeSortPoints


def run(
        src: Path,
        dst_dir: Path,
        seed: int,
        file_header: str
):
    """
    Symbolically combine polynomials and then evaluate for various evaluation sets.
    :param src: Data input path or directory
    :param dst_dir: Data output CSV path or directory where CSVs will be saved
    :param seed: Random number seed
    :param file_header: Header to add to top of output CSV
    """

    # Read data check, among other things, that m <= n
    input_params: dict = read_input_params(src)

    # Iterate over each n, m pair
    for n, m in input_params.items():

        # Generate sequence of randomly dispersed points
        data_maker = DataMaker(n, seed=seed)
        P: List[list] = data_maker.make_data()

        # Compute distances among points
        distance_computer = DistanceComputer(P)
        distances: List[dict] = distance_computer.compute_distances()

        # Sort points
        merge_sort_points = MergeSortPoints(distances)
        P_sorted = merge_sort_points.sort()

        # Select nearest m pairs
        P_selected = P_sorted[:m]

        # Process outputs





        # Compute distances




        file_io = FileIO(src, dst_dir)
        datasets = file_io.read_input()
        if len(datasets) == 0:
            raise ValueError("No files were read.")

        # Metrics table: Add number of comparisons, exchanges, and partition calls
        metrics_table = [
            ["presort_n", "presort", "n", "metric", "unsorted", "heap_sort", "two_way_merge", "three_way_merge",
             "four_way_merge", "natural_merge"]]

        # Iterate over each dataset
        for dataset_name, dataset in datasets.items():
            print(f"Dataset: {dataset_name}")
            data_dict = {"unsorted": dataset}

            # Iterate over each sorter (e.g., 2-way merge sort, natural merge, etc.)
            for sort_name, sorter_di in sorters.items():
                print(f"\tSort: {sort_name}")
                # Extract dictionary arguments, instantiate sorter, and sort list
                sorter_class, kwargs = sorter_di["sort_class"], sorter_di["kwargs"]
                sorter = sorter_class(deepcopy(dataset), **kwargs)
                sorter.sort()

                # Build temp dictionary and add outputs
                data_dict[sort_name] = {"sorted": sorter.sorted_li,
                                        "n": sorter.n,
                                        "n_comparisons": sorter.n_comparisons,
                                        "n_exchanges": sorter.n_exchanges,
                                        "n_partition_calls": sorter.n_partition_calls,
                                        "elapsed_ns": sorter.elapsed}

            # Make destination filepath
            dst = file_io.create_out_filename(dataset_name)

            # Make file headers
            operation_message = "Unsorted and sorted lists and sorted list performance metrics."
            in_file = src / f"{dst.stem}.dat"
            file_header_ = make_header(file_header, in_file, dst, operation_message)

            # Make column names
            column_names: list = list(data_dict.keys())

            # Create metrics table
            csv_li: list = [["metric"] + column_names]

            # Metrics table: Add number of comparisons, exchanges, and partition calls
            for metric in ["n", "n_comparisons", "n_exchanges", "n_partition_calls", "elapsed_ns"]:
                li = [di[metric] for k, di in data_dict.items() if k != "unsorted"]
                if metric == "n":
                    metric_li = [metric, len(dataset)] + li
                else:
                    metric_li = [metric, "N/A"] + li
                csv_li.append(metric_li)
                metrics_table.append([dataset_name, dataset_name[:3], len(dataset)] + metric_li)

            csv_li.append([""] + len(column_names) * [""])  # blank line to separate tables

            # Create data table
            csv_li.append(["ix"] + column_names)
            counter = 0
            for ix, value in enumerate(data_dict["unsorted"]):
                li = [ix, value] + [sort_dict["sorted"][ix] for sort_name, sort_dict in
                                    data_dict.items() if sort_name != "unsorted"]
                csv_li.append(li)
                counter += 1

                # We don't need to write all the rows
                if counter >= 50:
                    break

            # Write outputs to CSV
            with open(str(dst), "w") as f:
                f.write(file_header_)
                writer = csv.writer(f)
                writer.writerows(csv_li)

        # Write standalone metrics table to file (for bulk processing only)
        metrics_table_dst = dst.parents[0] / "metrics_summary.csv"
        with open(str(metrics_table_dst), "w") as f:
            f.write(file_header + "\n")
            writer = csv.writer(f)
            writer.writerows(metrics_table)
