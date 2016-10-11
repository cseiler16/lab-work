# -*- coding: utf-8 -*-
from cStringIO import StringIO
import gzip as gz

import requests

family = 'RF02535'

URL = 'http://rfam.xfam.org/family/' + family + '/alignment/stockholm?gzip=1&download=1'
response = requests.get(URL)
sio = StringIO(response.content)
stockholm = gz.GzipFile(fileobj=sio).read()
#print(stockholm)

URL = 'http://rfam.xfam.org/family/' + family + '/alignment/fasta?gzip=1&download=1'
response = requests.get(URL)
sio = StringIO(response.content)
fasta = gz.GzipFile(fileobj=sio).read()
#print(fasta)

stockholmopen = stockholm
lhs, rhs = stockholmopen.split("#=GC SS_cons       ")
splitstock = rhs
lhs, rhs = splitstock.split("#=GC RF")
#print lhs
#splits the cons line from the rest of the string
stockholmstr = lhs
stockholmstr = stockholmstr.replace('<', '(').replace('>',')').replace(':','.').replace(',','.').replace('_','.').replace('[','(').replace(']',')').replace('-','.').replace(' ','')
#corrects stockholm format cons line for input into JAR3D
print stockholmstr
#outputfile.write(stockholmstr)


fastaopen = fasta
fastasplit = fastaopen.split('\n')
d = ">"
for line in fastasplit:
    s =  [e+d for e in line.split(d) if e != ""]
#print fastasplit

#outputfile.write(arg)

fastalongline = ''
currentheader = ''
currentline = ''

for item in fastasplit:
   if item.startswith('>'):
        if len(currentline) > 0:
            oksequence = 1
            for c in currentline:
                if not c in 'ACGU-':
                    oksequence = 0
            if oksequence == 1:
            # add code here to check if the sequence is only ACGU- and if so, add to fastalongline
                fastalongline += currentheader + '\n' + currentline + '\n'
        currentheader = item
        currentline = ''
   else:
       currentline += item
fastalongline += currentheader + '\n' + currentline + '\n'
fastalongline = stockholmstr + fastalongline

print(fastalongline)

filename = family + '_fasta.txt'
outputfile = open(filename,'w')
outputfile.write(fastalongline)
outputfile.close()
print('Wrote ' + filename)

# see if you can submit fastalongline directly to the JAR3D website.  That would be cool!

# if you are still pasting things into JAR3D by hand, perhaps write out a line that you can paste in to the search title so the Rfam family will be identified.
