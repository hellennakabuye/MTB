# MTB

These scripts are part of a major Django web application that analyses Mycobacterium tuberculosis sequence for the drug susceptibility profile, and produces a PDF file containing results.

The file.sh contains shell/bash script that analyses the input fasta file using mykrobe (http://www.mykrobe.com/)

The views.py file contains the preprocessing code for the input fasta file using SeqIO of Biopython and then analyses the results of the file.sh script to output a PDF file of the results.

The results file contains the anti-TB drugs and R for resistance or S for susceptible.

For any queries or improvements: hellennakabuye23@gmail.com
