import sympy as sp
from grafica import show
from p3_mapping import punto3_mapping

def punto3_tuning():
    Mf,wc_min,d_t,n_t,k,G=punto3_mapping()
    s = sp.symbols('s', complex=True)

    #alziamo un po' il gain per iniziare da più in alto
    Rs=k*50

    #in base al diagramma di bode aggiungiamo uno zero a 5 per alzare la fase nella zona di crossover
    Rd= 1+(1/5)*s

    #aggiungiamo un polo a 5000 per la fisica realizzabilità e per il disturbi in alte frequenze
    Rd= Rd/(1+(1/5000)*s)

    return Mf,wc_min,d_t,n_t,Rs,Rd,G

if __name__=='__main__':
    Mf,wc_min,d_t,n_t,Rs,Rd,G=punto3_tuning()
    print(f"regolatore statico: {Rs}")
    print(f"regolatore dinamico: {Rd}")
    show(Rs*Rd*G,Mf=Mf,wc_min=wc_min,d_t=d_t,n_t=n_t)
