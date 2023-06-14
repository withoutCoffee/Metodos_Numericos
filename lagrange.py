from sympy import symbols, simplify, Eq
import matplotlib.pyplot as plt

# Criação dos símbolos simbólicos
xi = symbols('x')

def lagrange_interpolation(x, y, x_val):
    n = len(x)
    result = 0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term

    # Substituição do valor x_val no polinômio interpolador
    value = result.subs(xi, x_val)

    return result,value

x = [1,5,10,12]
y = [4,20,9,15]
p = 6
r,v = lagrange_interpolation(x, y, p)

plt.title(f"polinomio:{r}")
plt.plot(x,y)
plt.scatter(p,v,color='r',label=f'Valor em P={p} ->{v}')
plt.legend()
plt.show()