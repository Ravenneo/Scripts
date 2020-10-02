# Scripts
This repository is a collection of Python/Biopython based scripts written with a specific scientific problem in mind

Please remember that these scripts were written by a self-taught beginner,you're welcome to use them but  use with caution!

1)


2) 	ETNA (EfeTch aNd pArse): Python based script that uses the Entrez util Efetch to fetch the  Identical Protein Groups (IPG) report for a list of proteins IDs. The retrieved report will be parsed using Pandas in order to only select entries that are from the Refseq NCBI database. Run the script as follows:
python etna.py <your_email> <file_with_protein_IDs.csv>
Note: This script is part of the bigger script arcane.py
