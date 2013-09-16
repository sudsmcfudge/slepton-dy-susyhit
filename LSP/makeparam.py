#!/usr/bin/env python

# M1,(M2), A_t, A_b, mu, MA, M_q3L, M_tR

from numpy import *

n = 100;

#ma  = linspace(1000,10000,n);
ma = [2000.]*n

#M1 = 100.0;
#M1 = ma/3.0;
M1  = linspace(0.26,1,n)*2000.;
#M2 = [100.0]*n;
#M2 = ma;
#M2  = linspace(2000,10000,n);
M2 = ma;

#mu  = ma;
mu = [100.0]*n

#tanb = 10.0;
tanb = 3.0;

#A_t = -2000.0;
#A_t = 0.0;
#A_t = 2000.0;

#M_L  = logspace(log10(80), log10(600.), n);
#M_R  = logspace(log10(80), log10(600.), n);

M_L = [500.]*n
M_R = [500.]*n

#min mixing X_t = 0
#A_t = ones(n)*mu/tanb;

#max mixing X_t = sqrt(6)*M_S
A_t = 0.0
#A_t = sqrt(6)*sqrt(M_q3L*2000.) + mu/tanb;

print n

#for i in range(n):
#    print M1, M2, A_t, mu, ma, tanb, M_L[i], 2000. #M_R[i] #M_q3L = M_tR

for i in range(n):
    print M1[i], M2[i], A_t, mu[i], ma[i], tanb, M_L[i], 2000. #M_tR[-1] #M_tR = 2000

for i in range(n):
    print M1[i], M2[i], A_t, mu[i], ma[i], tanb, 2000., M_R[i] #M_q3L = 2000
