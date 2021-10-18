"""Peter Rasmussen, Lab 4, parsers/file_io.py

This module reads an input file and organizes its contents into a dictionary of lists.
"""

# Standard library imports
import csv
import json
from pathlib import Path
from typing import List, Union

# Local imports
from pa1.utils import n_choose_k


class ReadDatasetError(Exception):
    pass


def read_input_params(in_file: Union[str, Path]) -> List[List[Union[int, float]]]:
    """
    Read integers from file input and append them to a list.
    in_file: Input file to read
    :return: List populated with data
    """
    # Convert in_file to Path object if string
    in_file = Path(in_file)

    # Check that in_file exists
    if not in_file.exists():
        raise FileNotFoundError(f"Input file {in_file} does not exist.")

    # Read in_file data
    with open(str(in_file), "r") as f:
        rows = f.readlines()

    # Iterate over each row and process n and m
    in_data = []
    line = 0

    for row in rows:
        line += 1
        n, m = row.replace("\ufeff", "").replace("\n", "").split(",")[:2]

        # Test if header columns are `n` and `m`, in that order
        if line == 1:
            if (n != "n") or (m != "m"):
                print(n, m)
                msg = f"{in_file}, line 1: Header row must include `n` & `m` as its 1st & 2nd cols."
                raise ReadDatasetError(msg)
            else:
                continue

        # Test if n and m values are non-negative integers
        if (not n.isdigit()) or (not m.isdigit()):
            msg = f"{in_file}, line {line}: n={n} and m={m} must be non-negative integers."
            raise ValueError(msg)

        # Convert n and m from strings to integers so we can complete the tests
        n, m = int(n), int(m)

        # Test if m <= n choose 2
        n_choose_2 = n_choose_k(n, 2)
        if m > n_choose_2:
            msg = f"{in_file}, line {line}: m = {m} but must be <= to n-choose-2 = {n_choose_2}."
            raise ValueError(msg)

        # Test if n > 1
        if n < 2:
            raise ValueError(f"{in_file}, line {line}: n is {n} but must be greater than 1.")

        # Test if m > 0
        if m < 1:
            raise ValueError(f"{in_file}, line {line}: m is {m} but must be greater than 0.")

        # Append n and m to list
        in_data.append([n, m])

    return in_data


def write_closest_pairs_outputs(dst: Path, closest_pairs_output: List[dict]):
    """
    Write closest pairs output: The m-closest pairs along with all n original points included
    :param dst: JSON path
    :param closest_pairs_output: Includes n, m, m-closest pairs, and original set of points
    """
    with open(dst, "w") as f:
        json.dump(closest_pairs_output, f)


def write_stats_outputs(dst: Path, file_header: str, stats_output: List[List]):
    """
    Write statistical outputs.
    :param dst: CSV path
    :param file_header: CSV header
    :param stats_output: List of lists
    :return:
    """
    with open(dst, "w") as f:
        f.write(f"# {file_header}\n")
        writer = csv.writer(f)
        writer.writerows(stats_output)
