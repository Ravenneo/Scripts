#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd


file_name = sys.argv[1]
file_name_output = sys.argv[2]
df = pd.read_csv(file_name, sep="\t", low_memory=False)
# Get names of indexes for which rows have to be dropped
indexNames = df[ df['Protein Name'] == 'hypothetical protein'].index
# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)
#Filter out the capital H
indexNames = df[ df['Protein Name'] == 'Hypothetical protein'].index
df.drop(indexNames , inplace=True)   
                 
#write out the file with all the assemblies
df.to_csv (file_name_output + "_all_the_assemblies.tsv", "\t", index=False)
#write out file with only one representative for each WP_xxx
df2=df.sort_values(by = "Protein", axis=0, ascending=True, inplace=False).drop_duplicates(subset=['Protein'],keep='first').to_csv(file_name_output + "_one_WP_per_assembly.tsv", "\t", index=False)



print ('program finished')
