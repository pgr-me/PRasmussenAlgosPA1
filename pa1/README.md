# Peter Rasmussen, Programming Assignment 1

This Python 3 program finds the m nearest pairs of n randomly generated, two-dimensional points.

## Getting Started

The package is designed to be executed as a module from the command line. The user must specify the
input file path and output directory as illustrated below. The PRasmussenAlgosPA1/resources
directory provides example input and output files for the user. The
PRasmussenAlgosPA1/resources/inputs/default.csv file provides 24 n-m combinations.

```shell
python -m path/to/pa1 -i path/to/in_file.csv -o path/to/out_dir/ 
```

Optionally, the user may specify a file header that is prepended to the outputs. The example below
illustrates usage of the optional argument.

```shell
python -m path/to/pa1 -i path/to/in_file.csv -o path/to/out_dir/ -f "Your Header"
```

Finally, the user may specify the random seed used to generate the randomly distributed set of
points, as the example below shows.

```shell
python -m path/to/pa1 -i path/to/in_file.csv -o path/to/out_dir/ -s 777
```

A summary of the command line arguments is below.

Positional arguments:

    -i, --src          Input File or Directory Pathname
    -o, --dst_dir      Output File or Directory Pathname

Optional arguments:

    -h, --help          Show this help message and exit
    -f, --file_header   Input custom file header above output file
    -s, --seed          Provide pseudo-random seed

## Key parts of program
* DataMaker: Class that ingests a set of n-m combinations and, using (an optionally-provided) random seed, generates a random set of points.
* DistanceComputer: Class that computes the distance between each pair of points.
* HeapSort: Class that sorts the points list by distance.

## Features

* Capability to process one or more n-m combinations per run.
* Performance metrics for each run for each algorithm: number of distance comparisons, number of
  heapifies, and total number of operations (distance comparisons + n number of heapifies).
* Tested on inputs of up to n=1024 and m=523,776.
* Outputs provided as two files: 1) CSV of performance metrics and 2) JSON of echoed inputs and
  selected outputs.
* Control over randomization by selection of random seed.

## Input and Output Files

The ```resources/inputs``` directory contains the set of input files. Pre-processed outputs are in
the ```resources/outputs``` directory.

## Example Output Files

An example of the first few lines of the default.csv file is reproduced below. Each row represents a
run. We capture n, m, the number of distance comparisons, the number of heapifies, and the total 
number of operations in the n, m, dist_comps, n_heapifies, and total_ops columns, respectively.

**n**|**m**|**dist\_comps**|**n\_heapifies**|**total\_ops**
:-----:|:-----:|:-----:|:-----:|:-----:
2|1|1|0|1|
4|6|6|3|9
8|28|28|14|42
16|120|120|60|180

The default.JSON output echoes the randomized data made by DataMaker and also presents the m-nearest
point pairs.

## Sources

The heap sort method is adapted from the following source.
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms.
    Cambridge: The MIT Press.

## Licensing

This project is licensed under the CC0 1.0 Universal license.
