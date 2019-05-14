from sympy import *
import numpy as np

t = Symbol('t')

Catot = 90
Prtot 120
RhoEr = 0.1
RhoM = 0.1
BetaEr = 0.0025
BetaM = 0.0025
Kch = 4100
Kpump = 20
Kleak = 0.05
Kin = 300
Kout = 125
Km = 0.00625
Kplus = 0.1
Kmin = 0.01
K1 = 5
K2 = 0.8
K3 = 5

def Jpump(t):
    Kpump*Cacyt(t)

def Jch(t):
    Kch*((Cacyt(t)^2)/(K1^2 + Cacyt(t)^2))*(CaEr(t) - Cacyt(t))

def Jleak(t):
    Kleak *(CaEr(t) - Cacyt(t)),

def Jin(t):
    Kin*(Cacyt(t)^8)/(K2^8 + Cacyt(t)^8),

def Jout(t):
    (Kout * Cacyt(t)^2/(K3^2 + Cacyt(t)^2) + Km)* CaMyto(t)};

def dCacyt(t):
    Jch(t) + Jleak(t) - Jpump(t) + Jout(t) - Jin(t) + Kmin * CaPr(t) -
    Kplus *Cacyt(t) * Pr(t)

def dCaEr(t):
    (BetaEr / RhoEr) * (Jpump(t) - Jch(t) - Jleak(t))


def dCaMyto(t):
    (BetaM / RhoM) * (Jin(t) - Jout(t))

def CaPr(t):
    -Cacyt(t) - (RhoEr / BetaEr) * CaEr(t) - (RhoM / BetaM) * CaMyto(t) - Catot,

def Pr(t):
    Prtot - CaPr(t),

Cacyt[0] ==   0.3
CaEr[0] ==     0.2
CaMyto[0] ==   1
Cacyt = 
# eqs = {Cacyt'(t) ==
#     Jch(t) + Jleak(t) - Jpump(t) + Jout(t) - Jin(t) + Kmin*CaPr(t) -
#      Kplus*Cacyt(t)*Pr(t),
#    CaEr'(t) == (BetaEr /RhoEr)*(Jpump(t) - Jch(t) - Jleak(t)),
#    CaMyto'(t) == (BetaM/RhoM)*(Jin(t) - Jout(t)),
#    CaPr(t) ==
#     Catot - Cacyt[
#       t] - (RhoEr * CaEr(t) / BetaEr) - (RhoM * CaMyto(t)/BetaM),
#    Pr(t) ==
#     Prtot - (Catot -
#        Cacyt(t) - (RhoEr * CaEr(t) / BetaEr) - (RhoM *
#          CaMyto(t)/BetaM)),
#    Cacyt[0] == 0.3,
#    CaEr[0] == 0.2,
#    CaMyto[0] == 1};



sol = NDSolve[eqs /. fluxes /. params,
  {Cacyt(t), CaEr(t), CaMyto(t)},
  {t, 100, 300}]
