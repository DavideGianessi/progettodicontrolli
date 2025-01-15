import sympy as sp

def punto1():
    x1, x2 = sp.symbols('x1 x2')    # x1=theta x2=omega
    u = sp.symbols('u')
    theta_eq=sp.rad(120)
    J=800
    beta=0.6
    alpha=sp.rad(30)
    k=100

    tau = sp.cos(alpha) / ( 1 - ( sp.sin(alpha) * sp.cos(x1) )**2 )
    f1 = x2
    f2 = ( tau * u - beta * x2 - k * x1 ) / J
    h = x1

    f= sp.Matrix([f1,f2])
    h= sp.Matrix([h])

    equilibrio = sp.solve(f, (x1,x2,u),dict=True)[0]
    equilibrio[x1]=theta_eq
    equilibrio = { var: expr.subs(x1,theta_eq) for var, expr in equilibrio.items() }

    #matrici di stato
    A = f.jacobian([x1,x2]) # Derivata di f rispetto a x
    B = f.jacobian([u])     # Derivata di f rispetto a u
    C = h.jacobian([x1,x2]) # Derivata di h rispetto a x
    D = h.jacobian([u])     # Derivata di h rispetto a u

    A = A.subs(equilibrio)
    B = B.subs(equilibrio)
    C = C.subs(equilibrio)
    D = D.subs(equilibrio)

    return f,h,equilibrio,A,B,C,D

if __name__ == '__main__':
    f,h,equilibrio,A,B,C,D=punto1()
    print("x' = f(x,u):")
    sp.pprint(f,use_unicode=True)
    print("")
    print("y = h(x,u):")
    sp.pprint(h,use_unicode=True)
    print("")
    print("coppia di equilibrio:")
    sp.pprint(equilibrio)
    print("")
    print("Matrice A:")
    sp.pprint(A)
    print("")
    print("\nMatrice B:")
    sp.pprint(B)
    print("")
    print("\nMatrice C:")
    sp.pprint(C)
    print("")
    print("\nMatrice D:")
    sp.pprint(D)
