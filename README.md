# Scripts
This repository is a collection of small/basic Python/Biopython based scripts written with a specific scientific problem/need in mind

Please remember that these scripts were written by a self-taught beginner,you're welcome to use them but  use with caution!

1)


2) **etna.py(EfeTch aNd pArse)**: Python based script that uses the Entrez util Efetch to fetch the  Identical Protein Groups (IPG) report for a list of proteins IDs. The retrieved report will be parsed using Pandas in order to only select entries that are from the Refseq NCBI database. Run the script as follows:
*python etna.py <your_email> <file_with_protein_IDs.csv>*

  Note: This script is part of the bigger script arcane.py

3) **get_fasta.py**:  Python based script that uses the Entrez util Efetch to download the protein Fasta sequence for a list of proteins IDs. Run as follows:
*python get_fasta.py <your_email> <file_with_protein_IDs.csv>*

4) **get_fasta_DNA.py**:  Python based script that uses the Entrez util Efetch to download the DNA Fasta sequence for a list of nuccore IDs. Run as follows:
*python get_fasta_dna.py <your_email> <file_with_protein_IDs.csv>*




***Dependencies: For Scripts from 2-x, Biopython is needed. Additionally, arcane.py require a local installation of HMMER***



## Reference
HMMER: Eddy SR. Accelerated Profile HMM Searches. Pearson WR, editor. PLoS Comput Biol. 2011;7: e1002195.
