"""Peter Rasmussen, Lab 4, parsers/file_io.py

This module reads an input file and organizes its contents into a dictionary of lists.
"""

# standard library imports
from collections import OrderedDict
from pathlib import Path
from typing import Union


class ReadDatasetError(Exception):
    pass


def read_input_params(in_file: Union[str, Path]) -> dict:
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
    in_data = OrderedDict()
    line = 0
    for row in rows:
        line += 1
        n, m = row.split(",")[:2]
        n = n.replace("\ufeff", "")
        m = m.replace("\n", "")

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

        # Test if m <= n
        if m > n:
            msg = f"{in_file}, line {line}: m is {m} but must be less than or equal to n {n}."
            raise ValueError(msg)

        # Test if n > 1
        if n < 2:
            raise ValueError(f"{in_file}, line {line}: n is {n} but must be greater than 1.")

        # Test if m > 0
        if m < 1:
            raise ValueError(f"{in_file}, line {line}: m is {m} but must be greater than 0.")

        # Populate ordered dictionary
        in_data[n] = m

    return in_data
