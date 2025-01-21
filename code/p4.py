import sympy as sp
from p3_tuning import punto3_tuning
import numpy as np
from scipy.signal import lti, impulse, step
from grafica import linear_sim

def punto4():
    _,_,_,_,Rs,Rd,G=punto3_tuning()
    s = sp.symbols('s', complex=True)

    L_s=Rs*Rd*G
    #gradino
    W_s=1/s
    #d_t
    t = sp.symbols("t")
    d_t=0
    for k in range(1,5):
        d_t+=0.2*sp.sin(0.1 * k * t)
    D_s=sp.laplace_transform(d_t,t,s)[0]
    #d_t
    t = sp.symbols("t")
    n_t=0
    for k in range(1,5):
        n_t+=0.2*sp.sin(10**5 * k * t)
    N_s=sp.laplace_transform(n_t,t,s)[0]

    F_s=L_s/(1+L_s)
    S_s=1/(1+L_s)

    Yw= F_s*W_s
    Yd= S_s*D_s
    Yn= -F_s*N_s

    return Yw,Yd,Yn,Rs,Rd,G

if __name__=='__main__':
    Yw,Yd,Yn,Rs,Rd,G=punto4()
    linear_sim(Yw,Yd,Yn)
