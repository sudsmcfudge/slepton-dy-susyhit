#!/usr/bin/env python

from numpy import arccos
import pickle
import sys


if len(sys.argv) != 3:
   print sys.argv[0], "<rundir> <output file>"
   exit(0)

rundir = sys.argv[1]
fname = sys.argv[2]

spectrumfn   = rundir + "/slhaspectrum.in"
susyhitfn    = rundir + "/susyhit_slha.out"
#fn = "../susyhit/susyhit_slha.out"

errorfile = open(spectrumfn)
# check for errorcodes

l = errorfile.readline()
while (not l.startswith('BLOCK SPINFO')):
    l = errorfile.readline()

l = errorfile.readline()
l = errorfile.readline()
l = errorfile.readline()
#print l

errordict = {}

if l.startswith('# Caution:'):
   l = errorfile.readline()
   while (not l.startswith('#')):
      s = l.split()
      errordict[int(s[0])] = l.split(s[0])[1].strip()
      l = errorfile.readline()
else:
   errordict[0] = "NO ERROR"

errorfile.close()

f = open(susyhitfn)
fout = open(fname, 'ab')

l = f.readline()
while (not l.startswith('BLOCK EXTPAR')):
    l = f.readline()

l = f.readline()
inputdict = {}

while (not l.startswith('#')):
    a = l.split()
    inputdict[int(a[0])] = {'value':float(a[1]), 'name':a[3]}
    l = f.readline()

#l = f.readline()

while (not l.startswith('BLOCK MASS')):
    l = f.readline()

l = f.readline() #block mass
l = f.readline() #header
massspect = {}

while (not l.startswith('#')):
    a = l.split()
    massspect[int(a[0])] = {'mass':float(a[1]), 'particle':a[3]}
    l = f.readline()

while (not l.startswith('BLOCK STOPMIX')):
    l = f.readline()

l = f.readline()
#print l
theta_stop = arccos(float(l.split()[2]))


def getDict(f, pdg):
    decay_string = "DECAY   " + str(pdg)

    l = f.readline()
    while (not l.startswith(decay_string) ):
        l = f.readline()

    d = {}
    flag = True

    #print "begin loop"
    l = f.readline()
    while (flag):
        if (l.startswith('#')):
            keys = l.split()
            if len(keys) > 1:
                keys.remove('#') # get rid of the '#'
                l = f.readline()
            else:
                flag = False
        else:
            s = l.split('#')
            s_temp = s[0].split()
            s_temp[0] = float(s_temp[0])            
            for i in range(1,len(s_temp)):
                s_temp[i] = int(s_temp[i])
            d[s[1].strip()]=dict(zip(keys,s_temp))
            l = f.readline()

    return d


selecL = getDict(f,1000011)
selecR = getDict(f,2000011)
snu  = getDict(f,1000012)
cha1 = getDict(f,1000024)
cha2 = getDict(f,1000037)
neu2 = getDict(f,1000023)
neu3 = getDict(f,1000025)
neu4 = getDict(f,1000035)

#print "stop1:"
#for i in stop1.itervalues():
#    print i

#print "stop2:"
#for i in stop2.itervalues():
#    print i

pickle.dump(errordict, fout)
pickle.dump(inputdict, fout)
pickle.dump(massspect, fout)
pickle.dump(selecL, fout)
pickle.dump(selecR, fout)
pickle.dump(snu, fout)
pickle.dump(cha1, fout)
pickle.dump(cha2, fout)
pickle.dump(neu2, fout)
pickle.dump(neu3, fout)
pickle.dump(neu4, fout)

fout.close()
f.close()
