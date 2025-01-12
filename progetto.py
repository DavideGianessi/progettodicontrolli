import sympy as sp
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def show(system):
    omega = np.logspace(-1,2,1000)
    w, mag, phase = signal.bode(system, omega)

    plt.figure(figsize=(10,6))

    #ampiezza
    plt.subplot(2,1,1)
    plt.semilogx(w, mag)
    plt.title("diagramma di bode")
    plt.xlabel("frequenza [rad/s]")
    plt.ylabel("Magnitudine [dB]")
    plt.grid(True)

    #fase
    plt.subplot(2,1,2)
    plt.semilogx(w, phase)
    plt.title("diagramma di bode")
    plt.xlabel("frequenza [rad/s]")
    plt.ylabel("fase [gradi]")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# Variabili di stato
x1, x2 = sp.symbols('x1 x2')
# x1=theta x2=omega

# Ingressi
u = sp.symbols('u')

# Parametri
theta_eq=sp.rad(120)
j=800
beta=0.6
alpha=sp.rad(30)
k=100

tau = sp.cos(alpha) / ( 1 - ( sp.sin(alpha) * sp.cos(x1) )**2 )
# Definizione delle funzioni non lineari
f1 = x2
f2 = ( tau * u - beta * x2 - k * x1 ) / j
h = x1

f= sp.Matrix([f1,f2])
h= sp.Matrix([h])

equilibrio = sp.solve(f, (x1,x2,u),dict=True)[0]
equilibrio[x1]=theta_eq

print("coppie di equilibrio:")
sp.pprint(equilibrio)


equilibrio = { var: expr.subs(x1,theta_eq) for var, expr in equilibrio.items() }

print("valori numerici:")
sp.pprint(equilibrio)

#matrici di stato
A = f.jacobian([x1,x2]) # Derivata di f rispetto a x
B = f.jacobian([u])     # Derivata di f rispetto a u
C = h.jacobian([x1,x2]) # Derivata di h rispetto a x
D = h.jacobian([u])     # Derivata di h rispetto a u

A = A.subs(equilibrio)
B = B.subs(equilibrio)
C = C.subs(equilibrio)
D = D.subs(equilibrio)

print("Matrice A:")
sp.pprint(A)

print("\nMatrice B:")
sp.pprint(B)

print("\nMatrice C:")
sp.pprint(C)

print("\nMatrice D:")
sp.pprint(D)

# variabile complessa s
s = sp.symbols('s', complex=True)

I = sp.eye(A.shape[0])

# calcolo la funzione di trasferimento G
G = C * ( s * I - A ).inv() * B + D
G=G[0]

print("\nMatrice G:")
sp.pprint(G)

numeratore,denominatore = sp.fraction(G)
numeratore = [float(coef) for coef in sp.Poly(numeratore, s).all_coeffs()]
denominatore = [float(coef) for coef in sp.Poly(denominatore, s).all_coeffs()]
system = signal.TransferFunction(numeratore,denominatore)
show(system)

#guadagno
G_static= G.subs(s,0)
gain_static= float(abs(G_static))
print(gain_static)
k = 199 / gain_static

print("errore a regime:",1/(1+float(abs((k*G).subs(s,0)))))
numeratore,denominatore = sp.fraction(k*G)
#denominatore = denominatore *s*s
numeratore = [float(coef) for coef in sp.Poly(numeratore, s).all_coeffs()]
denominatore = [float(coef) for coef in sp.Poly(denominatore, s).all_coeffs()]
system = signal.TransferFunction(numeratore,denominatore)
show(system)
