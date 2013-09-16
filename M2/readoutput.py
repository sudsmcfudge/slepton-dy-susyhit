#!/usr/bin/env python

import pickle
from numpy import *
from matplotlib import pyplot as py

#fn = "output_mequal_M2_200_A0.pkl"
#fn = "output_M2_200_A0.pkl"
fn = "output_M2_200_slep.pkl"
fp = open(fn)

temp = fn.split(".")[0]
outfnbase = "plot" + temp.split("output")[1]

errorlist = list()
inputlist = list()
masslist = list()
selecLlist = list()
selecRlist = list()
cha1list = list()
cha2list = list()
neu2list = list()
neu3list = list()
neu4list = list()

N = int(fp.readline().strip())

for i in range(N):
    #get errorcode:
    errorcode = pickle.load(fp)
    if (errorcode.has_key(4)):
        #tachyonic stop
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
    else:
        #good data
        errorlist.append(errorcode)
        inputlist.append(pickle.load(fp))
        masslist.append(pickle.load(fp))
        selecLlist.append(pickle.load(fp))
        selecRlist.append(pickle.load(fp))
        cha1list.append(pickle.load(fp))
        cha2list.append(pickle.load(fp))
        neu2list.append(pickle.load(fp))
        neu3list.append(pickle.load(fp))
        neu4list.append(pickle.load(fp))

halfind = len(errorlist)
print "halfway", halfind

for i in range(N,2*N):
    #get errorcode:
    errorcode = pickle.load(fp)
    if (errorcode.has_key(4)):
        #tachyonic stop
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
        pickle.load(fp)
    else:
        #good data
        errorlist.append(errorcode)
        inputlist.append(pickle.load(fp))
        masslist.append(pickle.load(fp))
        selecLlist.append(pickle.load(fp))
        selecRlist.append(pickle.load(fp))
        cha1list.append(pickle.load(fp))
        cha2list.append(pickle.load(fp))
        neu2list.append(pickle.load(fp))
        neu3list.append(pickle.load(fp))
        neu4list.append(pickle.load(fp))

n = len(errorlist)
print n

mL = zeros(n)
mR  = zeros(n)
mh   = zeros(n)
mselecL  = zeros(n)
mselecR  = zeros(n)
mcha1 = zeros(n)
mcha2 = zeros(n)
mneu1 = zeros(n)
mneu2 = zeros(n)
mneu3 = zeros(n)
mneu4 = zeros(n)


for i in range(n):
    mL[i] = inputlist[i][31]['value']
    mR[i]  = inputlist[i][34]['value']
    mh[i]   = masslist[i][25]['mass']
    mselecL[i] = masslist[i][1000011]['mass']
    mselecR[i] = masslist[i][2000011]['mass']
    mneu1[i] = masslist[i][1000022]['mass']
    mneu2[i] = masslist[i][1000023]['mass']
    mcha1[i] = masslist[i][1000024]['mass']
    mneu3[i] = masslist[i][1000025]['mass']
    mneu4[i] = masslist[i][1000035]['mass']
    mcha2[i] = masslist[i][1000037]['mass']

# plotting BR
# lets do this simple one first
# for each key, check to see if its in the list
# if not, add key to the list
# add (x,y) pair to list

# lets find stop -> top chi1

#find the correct entry

#for x,y,BR in tuple:
#py.plot(x,y,BR)

def func(xinput, stoplist):
    keylist = list()
    tlist   = list()

    for i in range(len(xinput)):
        keys = stoplist[i].keys()
        for k in keys:
            if k not in keylist:
                keylist.append(k)
                tlist.append( ([],[]) )

            ind = keylist.index(k)
            x = xinput[i]
            y = stoplist[i][k]['BR']
            tlist[ind][0].append(x)
            tlist[ind][1].append(y)

    yarray = zeros([len(keylist), len(xinput)])

    for i in range(len(keylist)):
        for j in range(len(xinput)):
            if xinput[j] in tlist[i][0]:
                yarray[i][j] = stoplist[j][keylist[i]]['BR']
            
    return xinput, yarray, keylist



#xarray, yarray, keylist = func(m3sq[0:halfind], stop1list[0:halfind])
#xarray, yarray, keylist = func(mtR[halfind:], stop1list[halfind:])
#xarray, yarray, keylist = func(m3sq[0:halfind], stop2list[0:halfind])
#xarray, yarray, keylist = func(mtR[halfind:], stop2list[halfind:])

#for i in range(len(keylist)):
    #py.plot(xarray, yarray[i][:],'-o',label=keylist[i])
    #py.semilogy(xarray, yarray[i][:],'-o',label=keylist[i])
    #py.plot(tlist[i][0], yarray[i][:],'o',label=keylist[i])


#xlabel = 'm3sq'

#py.figure()
#py.scatter(m3sq[0:halfind], mh[0:halfind])
#py.scatter(m3sq[0:halfind], mt2[0:halfind])
#py.scatter(m3sq[0:halfind], mb1[0:halfind], marker='x')
#py.xlabel(xlabel)
#py.ylabel('mh')
#py.ylim([0,2500])

#outfn = outfnbase + "_" + xlabel + "_mh.eps"
#py.savefig(outfn)


#xlabel = 'm3sq'

#py.figure()
#py.scatter(m3sq[0:halfind], mt1[0:halfind])
#py.scatter(mtR[0:halfind], mt2[0:halfind])
#py.xlabel(xlabel)
#py.ylabel('mt1')
#py.ylim([0,2500])

#outfn = outfnbase + "_" + xlabel + "_mt1.eps"
#py.savefig(outfn)

#xlabel = 'm3su'

#py.figure()
#py.scatter(mtR[halfind:], mneu2[halfind:] - mneu1[halfind:])
#py.scatter(mtR[0:halfind], mt2[0:halfind])
#py.xlabel(xlabel)
#py.ylabel('mneu2 - mneu1')
#py.ylim([0,2500])



"""
xlabel = 'm3su'

py.figure()
#py.scatter(m3sq[0:halfind], mt1[0:halfind])
py.scatter(mtR[halfind:], mt1[halfind:])
py.xlabel(xlabel)
py.ylabel('mt1')
py.ylim([0,2500])

outfn = outfnbase + "_" + xlabel + "_mt1.eps"
py.savefig(outfn)
"""


stop_decays = ["~chi_10 t", "~chi_1+ b", "~chi_20 t",
               "~t_1    Z", "~t_1    h", "~b_1    W"]

sbottom_decays = ["~chi_10 b", "~chi_1- t", "~chi_20 b",
                  "~t_1    W", "blah", "blah1"]

#style            = ['-bo','-rs','-c^','-g*']
style            = ['-o','-s','-^','-*', '-d', '-p']


def allpositive(bb):
    boo = True
    for b in bb:
        if (b < 0):
            boo = False
            return boo
    return boo

def makeplots(titlebase):
    mass_array = mselecL[0:halfind]
    xlabel = 'm' + titlebase

    if titlebase == 'selecL':
        stoplist = selecLlist[0:halfind]
        important_decays = stop_decays
        mass_array = mselecL[0:halfind]
    elif titlebase == 'selecR':
        stoplist = selecRlist[halfind:]
        important_decays = stop_decays
        mass_array = mselecR[halfind:]
    elif titlebase == 'cha1':
        stoplist = cha1list[0:halfind]
        important_decays = stop_decays
        xlabel = 'mslep'
    elif titlebase == 'neu2':
        stoplist = neu2list[0:halfind]
        important_decays = stop_decays
        xlabel = 'mslep'
    else:
        print NOPE
        return

    xlabel = 'mslep'
    outfn = outfnbase + "_" + xlabel + "_" + titlebase + ".eps"

    py.figure(figsize=(16,12))
    ax1 = py.subplot(111)
    box1 = ax1.get_position()
    ax1.set_position([box1.x0, box1.y0, box1.width * 0.8, box1.height])

    xarray, yarray, keylist = func(mL[0:halfind], stoplist)

    xarray = mass_array

    indexlist = range(len(keylist))

    # to keep colors constant across graphs
    for d,s in zip(important_decays,style):
        for k in range(len(keylist)):
            #print keylist[k]
            if (d in keylist[k]):
                indexlist.remove(k)
                #print "blah", k
                if allpositive(yarray[k][:]):
                    py.semilogy(xarray, yarray[k][:],s,label=keylist[k])
                else:
                    py.semilogy(xarray, yarray[k][:],s,label=keylist[k])
                    print "hmm...", keylist[k], "< 0"
                    print yarray[k][:]

    #print indexlist
    #print keylist
    #print yarray

    for i in indexlist:
        if allpositive(yarray[i][:]):
            if len(keylist) > 7:
                if max(yarray[i][:]) > 5e-3:
                    py.semilogy(xarray, yarray[i][:],'-o',label=keylist[i])
            else:
                py.semilogy(xarray, yarray[i][:],'-o',label=keylist[i])
        else:
            py.semilogy(xarray, yarray[i][:],'-o',label=keylist[i])
            print "hmm...", keylist[i], "< 0"
            print yarray[i][:]

    py.title(titlebase + ' branching fractions')
    py.xlabel(xlabel)
    py.ylabel('BR')
    #py.xlim(200, 2100)
    py.ylim(0, 1.5)

    ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    py.savefig(outfn)

    

makeplots('selecL')
makeplots('selecR')
#makeplots('t2')
makeplots('cha1')
makeplots('neu2')



#py.legend(loc = 'upper right', bbox_to_anchor = (0, 1.0))

#py.figure()
#py.plot(m3sq,mh)

#py.figure()
#py.scatter(xarray, mt1[0:halfind])
#py.xlabel('m3sq')
#py.ylabel('mt1')

#py.figure()
#py.plot(m3sq,array(thetalist)*180.0/pi)

# error check
def errorcheck(errlist):
    bigerr = {}

    for d in errlist:
        keys = d.keys()
        for k in keys:
            if not bigerr.has_key(k):
                bigerr[k] = d[k]

    return bigerr

bigerr = errorcheck(errorlist)
#for d in errorlist:
#    print d.keys()

print bigerr

#print m3sq


py.show()


#br_ind = list()
#br_y = list()

#for i in range(n):
#    for d in stop2list[i].itervalues():
#        if (d['NDS'] == 2):
#            idlist = sort(d['ID1'], d['ID2'])
#        else:
#            idlist = sort(d['ID1'], d['ID2'], d['ID3'])
#            
#        if (d['ID1'] == 1000022 and d['ID2'] == 6):
#            br_ind.append(i)
#            br_y.append(d['BR'])
        
#py.figure()
#py.plot(m3sq[br_ind], br_y, 'o')
#py.figure()
#py.plot(mtR[br_ind], br_y, 'o')



#for i in stop1list[15]:
#    print i

#py.figure()
#py.scatter(m3sq, mt1, marker='x')
#py.scatter(m3sq, mt2, marker='o')
#py.figure()
#py.plot(mt1,mh,'.')
#py.plot(mt2,mh,'.')
#py.show()

#for i in masslist:
#    print i

#print inputlist

#print inputlist
#print masslist
#print stop1list
#print stop2list



fp.close()
