#!/usr/bin/env python
# coding: utf-8
import sys
import csv
from http.client import IncompleteRead
import pandas as pd
from Bio import Entrez
Entrez.email = sys.argv[1]

    

# get from WPs accession, corresponding assembly, NC IDs, strains names. Write a csv table with all these as final data tablee,
#+ a table with WPs and Assembly IDs for inputting in FLAG

list_of_accession = []
with open (sys.argv[2], 'r', encoding='utf-8-sig') as csvfile:
    efetchin=csv.reader(csvfile, delimiter = ',')
    for row in efetchin:
        list_of_accession.append(str(row[0]))
        
with open('efetch_output.txt', mode = 'w') as efetch_output:
    efetch_output = csv.writer(efetch_output, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    input_handle = Entrez.efetch(db="nuccore", id= list_of_accession, rettype="fasta")
    output_handle = open("efetch_output.txt", "a")
    for line in input_handle:
        output_handle.write(line)

input_handle.close()
output_handle.close()

print ('program finished')
