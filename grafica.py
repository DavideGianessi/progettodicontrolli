import numpy as np
import sympy as sp
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def show(G,Mf=None,wc_min=None, d_t=None, n_t=None):
    s = sp.symbols('s', complex=True)
    numeratore,denominatore = sp.fraction(G)
    numeratore = [float(coef) for coef in sp.Poly(numeratore, s).all_coeffs()]
    denominatore = [float(coef) for coef in sp.Poly(denominatore, s).all_coeffs()]
    system = signal.TransferFunction(numeratore,denominatore)
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

    if(d_t):
        d_t_rec= patches.Rectangle((0,0),0.5,d_t, color='red', alpha=0.3)
        ax1.add_patch(d_t_rec)
    if(wc_min):
        wc_min_rec= patches.Rectangle((0,-1000),wc_min,1000, color='red', alpha=0.3)
        ax1.add_patch(wc_min_rec)
    if(n_t):
        n_t_rec= patches.Rectangle((10**5,-n_t),10**8-10**5,1000, color='red', alpha=0.3)
        ax1.add_patch(n_t_rec)

    #fase
    ax2=plt.subplot(2,1,2)
    plt.semilogx(w, phase)
    plt.title("diagramma di bode")
    plt.xlabel("frequenza [rad/s]")
    plt.ylabel("fase [gradi]")
    plt.grid(True)

    ax2.set_ylim(-190,10)

    if(Mf):
        Mf_rec= patches.Rectangle((wc_min,-300),10**5-wc_min,300-180+Mf, color='red', alpha=0.3)
        ax2.add_patch(Mf_rec)

    plt.tight_layout()
    plt.show()
