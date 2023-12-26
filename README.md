# mchr1
Ph.D. thesis generator for mchr1

for PMID in $(esearch -db pubmed -query "mchr1" | efetch -format uid); do echo $PMID && \n    efetch -db pubmed -id $PMID -format abstract > "$PMID.txt"\ndone\n

esearch -db pubmed -query "mchr1" | efetch -format abstract > out-mchr1.txt\n

