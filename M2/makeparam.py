#!/usr/bin/env python

# M1,(M2), A_t, A_b, mu, MA, M_q3L, M_tR

from numpy import *

n = 25;

M1 = 100.0;
M2 = 200.0;
#M2 = 4e3;

mu  = 2e3;
#mu = 300.
ma  = 2e3;
tanb = 10.0;

#A_t = -2000.0;
#A_t = 0.0;
#A_t = 2000.0;

M_L  = logspace(log10(200), log10(600.), n);
M_R  = logspace(log10(200), log10(600.), n);

#min mixing X_t = 0
#A_t = ones(n)*mu/tanb;

#max mixing X_t = sqrt(6)*M_S
A_t = 0.0
#A_t = sqrt(6)*sqrt(M_q3L*2000.) + mu/tanb;

print n

#for i in range(n):
#    print M1, M2, A_t, mu, ma, tanb, M_L[i], 2000. #M_R[i] #M_q3L = M_tR

for i in range(n):
    print M1, M2, A_t, mu, ma, tanb, M_L[i], 2000. #M_tR[-1] #M_tR = 2000

for i in range(n):
    print M1, M2, A_t, mu, ma, tanb, 2000., M_R[i] #M_q3L = 2000
