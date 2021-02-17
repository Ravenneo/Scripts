__author__ = 'Dr Giusy Mariano'
__email__ = 'giusy.mariano@ncl.ac.uk'
__license__ = "GPL"
#!/usr/bin/env python
# coding: utf-8
import sys
import subprocess as sp
import csv
from Bio import SearchIO
import pandas as pd
from Bio import Entrez

print ('Can go for cup of coffee')
print ('Come back later to input min and max lenght for your parse...')

#initialize search function
def hmm_search(hmm_directory, protein_directory):

    

    hmmsearch = "hmmsearch" + " " + "-T 30" + " "+ "--incT 30" +" "+ "-o log"+ " --domtblout" +" "+ "HMM_output.txt" + " " + hmm_directory + " " + protein_directory

    sp.run(hmmsearch, shell=True)
    
    
    
if __name__ == '__main__':
    hmm_search(sys.argv[1],sys.argv[2])       #makes it take 2 args from command line 
    
    
    
    
x = int(input('min lenght'))
y = int(input('max lenght'))



    
with open('HMM_output.txt', newline ='') as input:
    for qresult in SearchIO.parse(input, 'hmmscan3-domtab'):
        query_id = qresult.id  
        query_len = qresult.seq_len
        hits = qresult.hits
        num_hits = len(hits)
        hits_len = qresult.seq_len
        
        if num_hits > 0 :
            with open('parsed_output.csv', mode='w') as parsed_output:   #write table for Suppl.data with hitsID, scores and lenght
                parsed_output = csv.writer(parsed_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                parsed_output.writerow(['hit_accession', 'hit_description', 'E-value', 'Bit Score', 'Hits_Lenght'])
            for i in range(0,num_hits): 
                hit_evalue = hits[i].evalue 
                hit_bit_Score = hits[i].bitscore
                hit_accession= hits[i].id
                hit_length = hits[i].seq_len
                hit_description = hits[i].description 
                if hit_length > x and hit_length < y:
                    with open('parsed_output.csv', mode='a') as parsed_output:   #write table for Suppl.data with hitsID, scores and lenght. Need mode 'a' to append to existing table
                        parsed_output = csv.writer(parsed_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)     
                        parsed_output.writerow([hit_accession,hit_description, hit_evalue,hit_bit_Score, hit_length])
                    with open('efetch_input.csv', mode='a') as efetch_input:   #write table with Hits IDs for FLAGS
                        efetch_input = csv.writer(efetch_input, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        efetch_input.writerow([hit_accession])
print ('HMMer_parse_complete')          
print ('efetch_start')
# get from WPs accession, corresponding assembly, NC IDs, strains names.
# Write a csv table with all these as final data tablee,
#+ a table with WPs and Assembly IDs for inputting in FLAG

Entrez.email = "raven.neo@gmail.com"

    

# get from WPs accession, corresponding assembly, NC IDs, strains names. Write a csv table with all these as final data tablee,
#+ a table with WPs and Assembly IDs for inputting in FLAG

list_of_accession = []
with open (sys.argv[1], 'r') as csvfile:
    efetchin=csv.reader(csvfile, delimiter = ',')
    for row in efetchin:
        list_of_accession.append(str(row[0]))
        
with open('efetch_output.tsv', mode = 'w') as efetch_output:
    efetch_output = csv.writer(efetch_output, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    efetch_output.writerow(['ID','Source', 'Nucleotide Accession', 'Start', 'Stop', 'Strand', 'Protein', 'Protein Name', 'Organism', ' Strain', 'Assembly'])
    input_handle = Entrez.efetch(db="protein", id= list_of_accession, rettype="ipg", retmode="tsv")
    output_handle = open("efetch_output.tsv", "wb")
    
    for line in input_handle:
        output_handle.write(line)
output_handle.close()
input_handle.close()
#process file in pandas
file_name = "efetch_output.tsv"
file_name_output = "final_output.tsv"
df = pd.read_csv(file_name, sep="\t", low_memory=False)
# Get names of indexes for which rows have to be dropped
indexNames = df[ df['Source'] == 'INSDC'].index
# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)
#rearrange table columns
df = df[['ID', 'Source', 'Nucleotide Accession', 'Protein', 'Protein Name', 'Start', 'Stop', 'Strand', 'Organism',' Strain', 'Assembly']]
#Sort table on Assembly number ignoring GCF_
df['sort'] = df['Assembly'].str.extract('(\d+)', expand=False).astype(float)
df.sort_values('sort',inplace=True, ascending=True)
df = df.drop('sort', axis=1)
#drop all duplicates that're similar in indicated subset fields
df3=df.drop_duplicates(subset=['Start', 'Stop', 'Strand', 'Organism',' Strain', 'Assembly'],keep='first')
#sorts dataframe alphabetically by Organism and writes to csv
df3.sort_values(by = "Organism", axis=0, ascending=True, inplace=False).to_csv("final_parsed_output.tsv", "\t", index=False)
#get WP_X and GFC_X IDs in a tsv to input in FLAGs
new_dataframe1 = df3[['Assembly', 'Protein']]
new_dataframe2 = df3[['Organism',' Strain', 'Assembly', 'Protein']]
new_dataframe1.sort_values(by = "Protein", axis=0, ascending=True, inplace=False).to_csv('flags_input.tsv', '\t', header=False, columns = ['Assembly', 'Protein'])
new_dataframe2.sort_values(by = "Organism", axis=0, ascending=True, inplace=False).to_csv('flags_input_wstrains.tsv', '\t', header=False, columns = ['Organism',' Strain', 'Assembly', 'Protein'])





print ('program finished')
