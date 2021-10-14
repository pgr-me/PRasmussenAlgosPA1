"""Peter Rasmussen, Lab 4, __main__.py

This program ingests files containing lists of integers, sorts those files using five different
algorithms, and saves an output for each processed file.

Header statements make up the first five lines of the output file. Beneath the header lines is a
performance metrics summary table, which includes list size, number of comparisons,
number of exchanges, number of recursive partition calls, and runtime.

Instructions for executing the program along with an example output file are provided in the README
in the root directory of the lab4 module.

The structure of this package is based on the Python lab0 package that Scott Almes developed for
this course. Per Scott Almes, this module "is the entry point into this program when the module is
executed as a standalone program."

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
    "--src", "-i", type=Path, help="Input file"
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
