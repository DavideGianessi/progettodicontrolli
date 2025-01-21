import sympy as sp
from grafica import show
from p3_mapping import punto3_mapping

def punto3_tuning():
    Mf,wc_min,d_t,n_t,k,G=punto3_mapping()
    s = sp.symbols('s', complex=True)

    Rs=k #regolatore statico

    wc_chosen=2*wc_min
    Mf_chosen=Mf+10
    Ge=Rs*G

    #formule di inversione
    M_star= 1/abs(Ge.subs({s: sp.I*wc_chosen}))
    phi_star= Mf_chosen-180-sp.deg(sp.arg(Ge.subs({s: sp.I*wc_chosen})))
    phi_star=sp.rad(phi_star)

    tau=(M_star-sp.cos(phi_star))/(wc_chosen*sp.sin(phi_star))
    alphatau=(sp.cos(phi_star)-(1/M_star))/(wc_chosen*sp.sin(phi_star))
    tau=tau.evalf()
    alphatau=alphatau.evalf()


    #rete anticipatrice
    Rd=(1+tau*s)/(1+alphatau*s)

    return Mf,wc_min,d_t,n_t,Rs,Rd,G

if __name__=='__main__':
    Mf,wc_min,d_t,n_t,Rs,Rd,G=punto3_tuning()
    print(f"regolatore statico: {Rs}")
    print(f"regolatore dinamico: {Rd}")
    R=Rs*Rd
    print("R:")
    sp.pprint(R)
    L=R*G
    print("L:")
    sp.pprint(L)
    show(Rs*Rd*G,Mf=Mf,wc_min=wc_min,d_t=d_t,n_t=n_t)
