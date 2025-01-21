import sympy as sp
from p2 import punto2
from grafica import show

def punto3_1():
    G=punto2()
    s = sp.symbols('s', complex=True)

    e_s=0.004 #<0.005
    #aggiusto l'errore a regime con il guadagno statico
    G_static= G.subs(s,0)
    gain_static= float(abs(G_static))
    k=(2/e_s)/gain_static
    return k,G

if __name__=='__main__':
    k,G=punto3_1()
    print(f"k: {k}")
    show(k*G)
