import sympy as sp
from p1 import punto1
from grafica import show

def punto2():
    _,_,_,A,B,C,D=punto1()

    s = sp.symbols('s', complex=True)
    I = sp.eye(A.shape[0])
    G = C * ( s * I - A ).inv() * B + D
    G=G[0]
    return G

if __name__ == '__main__':
    G=punto2()
    print("funzione di trasferimento:")
    sp.pprint(G)
    show(G)
