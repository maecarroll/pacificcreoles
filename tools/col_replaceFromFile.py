#
# Searches csv and replaces items in column from pattern file
# 
# Usage: python3 col_replace.py file.csv patternfile.csv column
#

import sys
import pandas as pd
import os

modfile = sys.argv[1]
patternfile = sys.argv[2]
column = int(sys.argv[3])

moddf = pd.read_csv(modfile, header=None)

#print(moddf)
with open(patternfile, 'r') as file:
    for line in file:
        line = tuple(str(x) for x in line.strip().split(','))
        pattern = '^' + line[0] + '$'
        moddf[column] = moddf[column].replace(pattern,line[1], regex=True)
    

output = str(modfile[0:-3]) + 'replaced.csv'

moddf.to_csv(output,index=False,header=False)