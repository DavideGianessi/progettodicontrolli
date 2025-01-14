import sympy as sp
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

def show(system):
    omega = np.logspace(-1,6,1000)
    w, mag, phase = signal.bode(system, omega)

    plt.figure(figsize=(10,6))

    #ampiezza
    ax1 = plt.subplot(2,1,1)
    plt.semilogx(w, mag)
    plt.title("diagramma di bode")
    plt.xlabel("frequenza [rad/s]")
    plt.ylabel("Magnitudine [dB]")
    plt.grid(True)

    ax1.set_ylim(-200,200)

    d_t = patches.Rectangle((0,0),0.5,40,color='red', alpha=0.3)
    ax1.add_patch(d_t)
    wc_min= patches.Rectangle((0,-1000),171.82,1000, color='red',alpha=0.3)
    ax1.add_patch(wc_min)
    d_n = patches.Rectangle((10**5,-63),10**8,1000,color='red', alpha=0.3)
    ax1.add_patch(d_n)


    #fase
    ax2=plt.subplot(2,1,2)
    plt.semilogx(w, phase)
    plt.title("diagramma di bode")
    plt.xlabel("frequenza [rad/s]")
    plt.ylabel("fase [gradi]")
    plt.grid(True)

    ax2.set_ylim(-190,10)

    Mf = patches.Rectangle((171.82,-300),10**5-171.82,300-180+89.24,color='red', alpha=0.3)
    ax2.add_patch(Mf)


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
#q: daje tutta per la funzione di trasferimento
#a: daje


print("Funzione di trasferimento G(s):")
sp.pprint(G)

#trovo i poli
numeratore,denominatore = sp.fraction(G)
res=sp.solve(sp.Eq(0,denominatore))
print("poli: ",res)
denominatore = [float(coef) for coef in sp.Poly(denominatore, s).all_coeffs()]
omega_n=math.sqrt(denominatore[-1])
print("omega_n: ",omega_n)
smorzamento= denominatore[-2] / (2*omega_n)
print("smorzamento: ",smorzamento)


numeratore,denominatore = sp.fraction(G)
numeratore = [float(coef) for coef in sp.Poly(numeratore, s).all_coeffs()]
denominatore = [float(coef) for coef in sp.Poly(denominatore, s).all_coeffs()]
system = signal.TransferFunction(numeratore,denominatore)
#show(system)


wc_min=171.82





#guadagno
G_static= G.subs(s,0)
gain_static= float(abs(G_static))
print(gain_static)
k = 199 / gain_static

print("errore a regime:",1/(1+float(abs((k*G).subs(s,0)))))
numeratore,denominatore = sp.fraction(k*G)
numeratore = [float(coef) for coef in sp.Poly(numeratore, s).all_coeffs()]
denominatore = [float(coef) for coef in sp.Poly(denominatore, s).all_coeffs()]
system = signal.TransferFunction(numeratore,denominatore)
show(system)
