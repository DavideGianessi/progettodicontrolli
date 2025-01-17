import sympy as sp
from p3_1 import punto3_1
from grafica import show
import math

def punto3_mapping():
    k,G=punto3_1()
    s = sp.symbols('s', complex=True)

    #sovraelongazione -> margine di fase
    s_star=2 #%
    xi = sp.symbols("xi") #smorzamento
    eq=sp.Eq(s_star/100,math.e**((-math.pi*xi)/sp.sqrt(1-xi**2))) #equazione per trovare xi
    solution=sp.solveset(eq, xi, domain=sp.S.Reals) #sp.solve() era troppo lento
    xi_star=float(list(solution)[0])
    Mf=100*xi_star

    #margine di fase da specifiche
    Mf=max(Mf,30)

    #tempo di assestamento -> wc_min
    Ta5=0.03
    wc_min= 3/(Ta5*xi_star) 

    #disturbi
    d_t=40
    n_t=63

    return Mf,wc_min,d_t,n_t,k,G

if __name__=='__main__':
    Mf,wc_min,d_t,n_t,k,G=punto3_mapping()
    print(f"margine di fase: {Mf}")
    print(f"wc_min: {wc_min}")
    show(k*G,Mf=Mf,wc_min=wc_min,d_t=d_t,n_t=n_t)
