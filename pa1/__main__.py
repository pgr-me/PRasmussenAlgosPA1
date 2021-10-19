"""Peter Rasmussen, Programming Assignment 1, __main__.py

This program selects the m closest pairs of points from a randomly-generated list of points in a two
dimensional plane. Closeness is measured using Euclidean distance, and m is less than or equal to n
choose 2.

Inputs: A default input, PRasmussenAlgosPA1/resources/inputs/default.csv, provides a set of n and m
values that the program generates outputs for.

Instructions for executing the program along with an example output file are provided in the README
in the root directory of the lab4 module.

The structure of this package is based on the Python lab0 package that Scott Almes developed for
Data Structures 605.202. Per Scott, this module "is the entry point into this program when the
module is executed as a standalone program."

Please note the default Python recursion depth needed to be modified (see line 31 below) so that the
maximum recursion depth would not be exceeded.

"""

# standard library imports
import argparse
from pathlib import Path
import sys

# local imports
from pa1.run import run


sys.setrecursionlimit(16000)


# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "--src", "-i", type=Path, help="Input CSV file"
)
parser.add_argument(
    "--dst_dir", "-o", type=Path, help="Output directory"
)
parser.add_argument(
    "--seed", "-s", default=777, type=int, help="Pseudo-random seed"
)
parser.add_argument(
    "--file_header",
    "-f",
    default="Peter Rasmussen: Programming Assignment 1",
    type=str,
    help="Specify file header",
)
args = parser.parse_args()

run(
    args.src,
    args.dst_dir,
    args.seed,
    args.file_header
)
