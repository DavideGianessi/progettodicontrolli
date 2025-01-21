import sympy as sp
from p1 import punto1
from grafica import show

def punto2():
    _,_,_,A,B,C,D=punto1()

    s = sp.symbols('s', complex=True)
    I = sp.eye(A.shape[0]) # Matrice identità di dimensione A.shape[0] (A.shape = (2,2))
    G = C * ( s * I - A ).inv() * B + D # Funzione di trasferimento
    G=G[0] # G è una matrice 1x1, quindi G[0] è l'unico elemento di G
    return G

if __name__ == '__main__':
    G=punto2()
    print("funzione di trasferimento:")
    sp.pprint(G)
    show(G)
