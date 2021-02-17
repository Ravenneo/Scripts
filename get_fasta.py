#!/usr/bin/env python
# coding: utf-8

import sys
import csv
from Bio import Entrez
Entrez.email = "raven.neo@gmail.com"

if len(sys.argv) < 3:
    print("It needs input and output arguments.")
    print("Ej: python get_fasta_L.py efetch.csv efetch_output.txt")
    sys.exit(0)

csv_file = sys.argv[1]
txt_file = sys.argv[2]

# get from WPs accession, corresponding assembly, NC IDs, strains names. Write a csv table with all
# these as final data tablee, + a table with WPs and Assembly IDs for inputting in FLAG

list_of_accession = []
with open(csv_file, 'r', encoding='utf-8-sig') as csvfile:
    efetchin=csv.reader(csvfile, delimiter = ',')
    for row in efetchin:
        list_of_accession.append(str(row[0]))

with open(txt_file, mode = 'w') as efetch_output:
    efetch_output = csv.writer(efetch_output, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    input_handle = Entrez.efetch(db="protein", id= list_of_accession, rettype="fasta")
    output_handle = open(txt_file, "a")
    for line in input_handle:
        output_handle.write(line)

input_handle.close()
output_handle.close()

print('program finished')
