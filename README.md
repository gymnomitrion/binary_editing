# binary_editing

####Create binary matrix from sets of RNA editing positions tables

Requirements:

Python 3 with installed: pandas, glob, numpy, itertools, os, sys


Usage:
Move to the directory containing only catalogues with RNA editing sites csv output files (see sample data).
Run Python script with argument providing name of output csv file e.g.

python /home/gymnomitrion/bimat_editing_sites.py results.csv

Test run:

Download and unzip 'liver_test.zip' for test dataset.
Change directory to 'liver_test'.
Run script specyfing the output filename (csv format):
python /path/to/bimat_editing_sites.py results.csv
