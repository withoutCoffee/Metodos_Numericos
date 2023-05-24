import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

from bissecao import bissec

# Teste de plot animado
a = math.pi/2
b = 3*math.pi/2

f = lambda x : math.sin(x)

p, x = bissec(f,a,b,10**-3,100)

lx = np.linspace(a,b,30)
y = [f(i) for i in lx]

fig, ax = plt.subplots()
def animate(i):
    ax.clear()
    
    # Grafico da função
    ax.plot(lx,y,label=f'Função Principal')
    ax.legend()
    # Pontos P de possível raiz
    ax.scatter(x[i],f(x[i]),color="red",label="Ponto p*")
    ax.legend()
ani = FuncAnimation(fig,animate,frames=len(x),interval = 300,repeat = False)
plt.show()
# print(lx)
# print(x)
# print(y)
# print(lx)