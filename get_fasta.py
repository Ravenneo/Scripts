__author__ = 'Dr Giusy Mariano'
__email__ = 'giusy.mariano@ncl.ac.uk'
__license__ = "GPL"
#!/usr/bin/env python
# coding: utf-8
import sys
import csv
from http.client import IncompleteRead
import pandas as pd
from Bio import Entrez
Entrez.email = sys.argv[1]

list_of_accession = []
with open (sys.argv[2], 'r', encoding='utf-8-sig') as csvfile:
    efetchin=csv.reader(csvfile, delimiter = ',')
    for row in efetchin:
        list_of_accession.append(str(row[0]))
        
with open('efetch_output.txt', mode = 'w') as efetch_output:
    efetch_output = csv.writer(efetch_output, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    input_handle = Entrez.efetch(db="protein", id= list_of_accession, rettype="fasta")
    output_handle = open("efetch_output.txt", "a")
    for line in input_handle:
        output_handle.write(line)

input_handle.close()
output_handle.close()

print ('program finished')
