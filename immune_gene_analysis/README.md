# Population genetics statistics (nucleotide diversity, Watterson’s θ and Tajima’s D)


This script will calculate the nucleotide diversity (π), Watterson’s θ and Tajima’s D for the specific sites in the genome
1) To run this script you will need allele frequency file for the population generated using VCFtools. 
2) a bed file named "windows.bed" in the same directory as the script. 
3) Specific sites/positions to be used as input. 
4) Know type of sites (4fold/0fold)to be analyzed
5) a working directory path

```
python Monarch_pi_tw_td_sfs_all_sites_1977.py
This script gives nucleotide diversity , watterson's theta  and Tajima's D  from allele frequency files. 
        For this you will need to have the follwoing files in a directory
        1) All positions for each codon position (codon1: codon_df_1.csv.gz; codon2: codon_df_2.csv.gz; codon3: codon_df_3.csv.gz; 4fold: codon_df_4d.csv.gz; 0fold: codon_df_0d.csv.gz;)
        2) for intergenic and all sites you will need to provide the refrence genome file as refrence.fa
        -F allele frequncy file (from VCF tools)
        -S input sites (CSV file with sites to be used)
        -I sites type (codon1/codon2/codon3/4fold/0fold)
        -P Path
        -Sec Section
```