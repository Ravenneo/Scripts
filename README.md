# Scripts
This repository is a collection of small/basic Python/Biopython based scripts written with a specific scientific problem/need in mind

Please remember that these scripts were written by a self-taught beginner,you're welcome to use them but  use with caution!

1) **arcane.py (hmmseARCh ANd parsE)**: Python based script that uses hmmsearch (from the HMMER suite (1)) to look for homologues of a protein of interest. It requires a local  fasta database and a hmm model of an alignment of homologues of the protein of interest (can be built with hmmbuild). The program subsequently parses the hits obtained by letting the user input a minimum and a maximum lenght for the proteins to include. The obtained list of proteins is then used as an input for the Entrez utils Efetch to fetch the Identical Protein Groups (IPG) report for a list of proteins IDs. The retrieved report will be parsed using Pandas in order to only select entries that are from the Refseq NCBI database. Script runs as follows: `python arcane.py <hmm_model> <database.fa> <example@email.com>`

2) **etna.py(EfeTch aNd pArse)**: Python based script that uses the Entrez utils Efetch to fetch the Identical Protein Groups (IPG) report for a list of proteins IDs. The retrieved report will be parsed using Pandas in order to only select entries that are from the Refseq NCBI database. Run the script as follows:
`python etna.py <example@email.com> <file_with_protein_IDs.csv>`

  Note: This script is part of the bigger script arcane.py

3) **get_fasta.py**:  Python based script that uses the Entrez util Efetch to download the protein Fasta sequence for a list of proteins IDs. Run as follows:
`python get_fasta.py <example@email.com> <file_with_protein_IDs.csv>`

4) **get_fasta_DNA.py**:  Python based script that uses the Entrez util Efetch to download the DNA Fasta sequence for a list of nuccore IDs. Run as follows:
`python get_fasta_dna.py <example@email.com> <file_with_protein_IDs.csv>`

5) **reptile.py**:  Python based  helper script. It is meant to be used after arcane.py or etna.py. From the output table of arcane.py or etna.py, it drops all the lines where proteins are annotated as 'hypothetical proteins'. Run as follows: `python reptile.py <file_with_IPG_report.csv>`

6) **get_taxonomy_data.py**: Python based script that uses Ete3 NCBI TAXA (2,3) to derive full descendand list starting from the TaxID of the Superkingdom rank. Pandas is then used to parse the output and eliminate unclassified organisms. The output of this is a file that can be uploaded in NCBI Common Tree (3) to obtain a tree of life with desidered organisms. The input file for the first script argument will be a list of Superkingdom rank TaxIDs. The second script argument is a the level of resolution desired for the tree (i.e. inpyt 'order' if the desired resolution level is order. Input 'species' if the desired level of resolution are species)
Run as : `python get_taxonomy_data.py <input_file.csv> <desired level of Tree resolution>`

7) **mario.py (hMmseARch hIts taxOnomy)**: Python based script that uses Ete3 NCBI TAXA (2,3) to derive full taxonomy of hits derived from arcane.py. Run as : `python mario.py <input_file_from_arcane.csv> <name_of_ouput_file.csv>`


***Dependencies: For Scripts from 1-7, Biopython is needed. Additionally, arcane.py require a local installation of HMMER***



## Reference
1)HMMER: Eddy SR. Accelerated Profile HMM Searches. Pearson WR, editor. PLoS Comput Biol. 2011;7: e1002195.
2)ETE 3: Reconstruction, analysis and visualization of phylogenomic data. Jaime Huerta-Cepas, Francois Serra and Peer Bork. Mol Biol Evol 2016; doi: 10.1093/molbev/msw046
3)Schoch CL, et al. NCBI Taxonomy: a comprehensive update on curation, resources and tools. Database (Oxford). 2020: baaa062
