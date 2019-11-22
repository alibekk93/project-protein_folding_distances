# Abstract

In addition to amino acid sequence, protein folding in cells depends on cellular environment, in-cluding chaperone proteins, cytoplasmic pH, temperature and ionic concentrations. Different or-ganisms, especially extremophiles, often have dissimilar cellular environments. Protein secondary structure identification methods regularly do not have these interspecific differences taken into consideration. As a result of that, known secondary structures determined for proteins from diverse organisms are often used for predictive methods training. Moreover, many protein structure studies use E. coli and other model organisms as expression systems for other species’ genes without considering of cellular environment factors. In order to assess the effect of species-specific factors, we analyzed protein folding in different cellular environments. During this study separate count matrices were created using structures of proteins with E. coli as expression system and compared with those with expression systems same as protein source organisms. Differences between count matrices from different models were quantified using Euclidean distances. Distances between the two T. thermophilus matrices were larger and more variable than those of non-thermophilic spe-cies. Moreover, we found directionality in this distance as helical secondary structures were more likely to form in T. thermophilus as expression system than in E. coli, where coil structures were formed instead. Our results suggest that extremophile protein source organisms should be used as protein expression systems in structural studies due to protein folding dependence on species-specific factors, such as environmental conditions and / or chaperone activity.

**This repository contains scripts used in the analysis**

### Order of procedure:
1) **Download [data](https://cdn.rcsb.org/etl/kabschSander/ss.txt.gz) from PDB.** This is a text file with chain IDs, amino acid sequences and secondary structure sequences for all residues available on PBD.
2) **Replace all " " in data file with "C".** PDB file has " " in positions with no stable structures (or coils). We replace these empty spaces with "C" so that later procedures work better and recognize the coil structueres properly.
3) **Create text files with sequence IDs for your databases.** Example of such file is [01_example_sequence_IDs]() in examples folder.
4) **Create database files using [DAMBE](http://dambe.bio.uottawa.ca/DAMBE/dambe.aspx) or use our files from databases folder.** Databases are in format:

|     |
| --- |
| >sequence_ID |
| AA_line |
| >sequence_ID |
| SS_line |

4) 
