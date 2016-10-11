# -*- coding: utf-8 -*-
#from Bio import SeqIO

#takes a stockholm and fasta file as inputs
outputfile = open("FASTA.txt", "r+")
stockholm = open("RF01725.stockholm.txt", "r+")
fasta = open("RF01725.afa.txt", "r+")

stockholmopen = stockholm.read()
lhs, rhs = stockholmopen.split("#=GC SS_cons       ")
splitstock = rhs 
lhs, rhs = splitstock.split("#=GC RF")
print lhs
#splits the cons line from the rest of the string

stockholmstr = lhs
stockholmstr = stockholmstr.replace('<', '(').replace('>',')').replace(':','.').replace(',','.').replace('_','.').replace('[','(').replace(']',')').replace('-','.').replace(' ','')
#corrects stockholm format cons line for input into JAR3D
print stockholmstr
outputfile.write(stockholmstr)

fastaopen = fasta.read()
fastasplit = fastaopen.split('\n')
d = ">"
for line in fastasplit:
    s =  [e+d for e in line.split(d) if e != ""]
print fastasplit

#outputfile.write(arg)

for item in fastasplit:
   if item.startswith('>'):
        outputfile.write('\n')
        outputfile.write(item + '\n') 
   else:
        outputfile.write(item)
        
stockholm.close()
fasta.close()
