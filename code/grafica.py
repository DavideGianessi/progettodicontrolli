import numpy as np
import sympy as sp
from scipy import signal
from scipy.signal import lti, impulse, step
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def show(G,Mf=None,wc_min=None, d_t=None, n_t=None):
    #passaggio della funzione di trasferimento a scipy
    s = sp.symbols('s', complex=True)
    numeratore,denominatore = sp.fraction(G)
    numeratore = [float(coef) for coef in sp.Poly(numeratore, s).all_coeffs()]
    denominatore = [float(coef) for coef in sp.Poly(denominatore, s).all_coeffs()]
    system = signal.TransferFunction(numeratore,denominatore)
    omega = np.logspace(-2,6,1000)
    w, mag, phase = signal.bode(system, omega)

    crossover_index = np.argmin(np.abs(mag))
    crossover_w = w[crossover_index]

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

    ax2.axvline(crossover_w,color='black')

    if(Mf):
        Mf_rec= patches.Rectangle((wc_min,-300),10**5-wc_min,300-180+Mf, color='red', alpha=0.3)
        ax2.add_patch(Mf_rec)

    plt.tight_layout()
    plt.show()

def linear_sim(Yw,Yd,Yn):
    s = sp.symbols('s', complex=True)
    Yw=sp.together(Yw)
    Yd=sp.together(Yd)
    Yn=sp.together(Yn)
    Ywnum,Ywden = sp.fraction(Yw)
    Ywnum = [float(coef) for coef in sp.Poly(Ywnum, s).all_coeffs()]
    Ywden = [float(coef) for coef in sp.Poly(Ywden, s).all_coeffs()]
    Ydnum,Ydden = sp.fraction(Yd)
    Ydnum = [float(coef) for coef in sp.Poly(Ydnum, s).all_coeffs()]
    Ydden = [float(coef) for coef in sp.Poly(Ydden, s).all_coeffs()]
    Ynnum,Ynden = sp.fraction(Yn)
    Ynnum = [float(coef) for coef in sp.Poly(Ynnum, s).all_coeffs()]
    Ynden = [float(coef) for coef in sp.Poly(Ynden, s).all_coeffs()]
    Tw = lti(Ywnum,Ywden)
    Td = lti(Ydnum,Ydden)
    Tn = lti(Ynnum,Ynden)

    t=np.linspace(0, 1,1000)

    _, yw = impulse(Tw, T=t)
    _, yd = impulse(Td, T=t)
    _, yn = impulse(Tn, T=t)

    y_total=yw+yd+yn

    plt.figure(figsize=(10, 6))

    ax=plt.subplot(1,1,1)

    ax.add_patch(patches.Rectangle((0,1.02),1,0.2,color='red',alpha=0.3))
    ax.add_patch(patches.Rectangle((0.03,1.05),1,0.2,color='green',alpha=0.3))
    ax.add_patch(patches.Rectangle((0.03,0),1,0.95,color='green',alpha=0.3))
    ax.add_patch(patches.Rectangle((0.8,0),0.2,0.995,color='blue',alpha=0.3))
    ax.add_patch(patches.Rectangle((0.8,1.005),0.2,0.2,color='blue',alpha=0.3))


    plt.plot(t, yw, label='yw')
    plt.plot(t, yd, label='yd')
    plt.plot(t, yn, label='yn')
    plt.plot(t, y_total, label='y_total', linestyle='--', linewidth=2)
    plt.title('System Responses')
    plt.xlabel('Tempo (s)')
    plt.ylabel('theta (rad)')
    plt.legend()
    plt.grid()
    plt.show()
