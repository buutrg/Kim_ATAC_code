#Run partition heritability conditioning on baseline and other annotations
#note that baseline has multiple versions (baseline_v1.2 is used here)


import os
import sys
import glob

i = sys.argv[1] #sumstats file
others = sys.argv[2] #full path to other annotation(s) to condition to (e.g., "/random/directory/annotation/allgenes/allgenes")
file = "/random/directory/annot/" #working directory that includes annotations
files = glob.glob("/random/directory/annot/*.22.annot.gz")
os.chdir(file)

for k in range(len(files)):
  j = files[k].split(file)[1][1:-12] #grab annotation names
  if (os.path.isfile("%s_%s_600.results" %(i, j)))==False: #unless LDSC already ran
  	print("python /random/directory/ldsc.py --h2 /random/directory/ldsc/sumstats_formatted/%s --ref-ld-chr /random/directory/ldsc/reference_files/1000G_EUR_Phase3/baseline_v1.2/baseline.,%s. --w-ld-chr /random/directory/ldsc/reference_files/1000G_EUR_Phase3/weights/weights.hm3_noMHC. --overlap-annot --frqfile-chr /random/directory/ldsc/reference_files/1000G_EUR_Phase3/plink_files/1000G.EUR.QC. --out %s_%s_600 --print-delete-vals --print-coefficients\"" % (i, others, i, j))
