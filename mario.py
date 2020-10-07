__author__ = 'Dr Giusy Mariano'
__email__ = 'giusy.mariano@ncl.ac.uk'
__license__ = "GPL"
#!/usr/bin/env python
# coding: utf-8
import csv
from ete3 import NCBITaxa
import pandas as pd
import sys

ncbi = NCBITaxa()

dicti= {}
input_phyla = []
phyla= []
temp=[]
phyla_ID=[]
#Import names of species from a file
with open (sys.argv[1], 'r') as csvfile:
    phylum = csv.reader(csvfile, delimiter = '\t')
    for row in phylum:
        input_phyla.append(row[1])
#translate the names to TaxIDs
i = 0
while i< len(input_phyla):
    name2taxid = ncbi.get_name_translator([input_phyla[i]])
    phyla.append(name2taxid)
    i+=1
#get only the values of this dictionary and put them in a new list
for d in phyla:
    for value in d:
        temp.append(d[value])
#flatten the list
for sublist in temp:
    for item in sublist:
        phyla_ID.append(item)                             



#get all the taxonomy info for FLAGS inputs
def get_desired_ranks(taxid, desired_ranks):
    lineage = ncbi.get_lineage(taxid)   
    names = ncbi.get_taxid_translator(lineage)
    lineage2ranks = ncbi.get_rank(names)
    ranks2lineage = dict((rank,taxid) for (taxid, rank) in lineage2ranks.items())
    return{'{}_id'.format(rank): ranks2lineage.get(rank, 'none') for rank in desired_ranks}

if __name__ == '__main__':

    desired_ranks = ['kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species','strain']
    #generate a list of lists for the results
    results = list()
    for taxid in phyla_ID:
        results.append(list())
        results[-1].append(str(taxid))
        ranks = get_desired_ranks(taxid, desired_ranks)
        for key, rank in ranks.items():
            if rank != 'none':
                results[-1].append(list(ncbi.get_taxid_translator([rank]).values())[0])
            else:
                results[-1].append(rank)
    #generate the header
    header = ['Original_query_taxid']
    header.extend(desired_ranks)
      

my_df = pd.DataFrame(results)
my_df.to_csv(sys.argv[2], sep = '\t', index=False, header=header)
