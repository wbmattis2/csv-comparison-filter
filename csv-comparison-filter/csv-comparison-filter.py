# CSV Comparison Filter, a tool for narrowing down records in one set of CSV files 
# to exclude those that are found in another set of CSV files.
# https://github.com/wbmattis2/csv-comparison-filter/
#
# MIT License
#
# Copyright (c) 2024 Benny Mattis
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import pandas as pd

# Change target_column_title to the title of the column by which records will be filtered
target_column_title = 'Email Address'
records_to_exclude = os.listdir('records-to-exclude')
files_to_filter = os.listdir('files-to-filter')

for current_file_to_filter in files_to_filter:
    result = pd.read_csv('files-to-filter/' + current_file_to_filter)
    result[target_column_title] = result[target_column_title].map(lambda x: str(x).strip())
    print( current_file_to_filter + ' initial count: {}'.format(result[target_column_title].count()) )
    for current_records_to_exclude in records_to_exclude:
        current_records_to_exclude = pd.read_csv('records-to-exclude/' + current_records_to_exclude)[target_column_title].map(lambda x: str(x).strip())
        result = result.loc[~result[target_column_title].isin(current_records_to_exclude)]
    print( current_file_to_filter + ' final count: {}'.format(result[target_column_title].count()) )
    result.to_csv( 'filtered-files/' + current_file_to_filter, index=False)
