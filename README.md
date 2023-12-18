# Kim_ATAC_code

Annotations available at https://alkesgroup.broadinstitute.org/LDSCORE/Kim_ATAC/



Source codes used for the primary analysis:

annotToLD_thinannot.py: make .ldscore.gz from .annot files

PartitionHeritability_baseline_others.py: run S-LDSC partition heritability given .annot and .ldscore.gz files (conditioning on the baseline model and other annotation(s))

PartitionHeritability_run.sh: run PartitionHeritability_baseline_others.py across multiple summary statistics



File formats:

.annot: thin-annot version is used (one column ANNOT)

.ldscore.gz: CHR, SNP, BP, L2 (delimiter = '\t')

For other details including creating annotations, please read the manuscript.


