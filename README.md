# Expense Tracker

CSV filtering tool built with Python by Benny Mattis.  

## Purpose

To filter sets of records against anther set of records, given CSV files containing said records.

## How to Use

Suppose you have two sets of records (i.e. rows), Set A and Set B. Records present in both Set A and Set B are "overlapping records." You want a set of records (Set C) containing all of Set A EXCEPT for the overlapping records.

Ensure that you have all of the records from Set A and Set B stored in CSV format.

Ensure that all the CSV files share a common column (e.g., a column containing email addresses) with the same column label (e.g., "Email Address") that can be used to determine whether records are overlapping. This is the "target column label."

Download the csv-comparison-filter folder. Edit line 31 of csv-comparison-filter.py to ensure that target-column-label is set to the target column label used to identify records in your CSV files. 

Place the files containing Set A in a folder named "files-to-filter," and place the files containing Set B in a folder named "records-to-exclude." Put both of these folders in the folder named csv-comparison-filter (alongside csv-comparison-filter.py).

Run csv-comparison-filter.py. Upon completion, versions of the "files-to-filter" files will be present in the "filtered-files" folder. The initial and final counts of records in each filtered file will be printed as output from Python.

## License

MIT License

Copyright (c) 2024 Benny Mattis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.