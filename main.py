import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Teste de plot animado
a = -10
b = 10

f = lambda x : x**2 + 3

x = np.arange(a,b,0.5)
y = f(x)

fig, ax = plt.subplots()

def animate(i):
    ax.clear()
    ax.plot(x,y)
    ax.scatter(x[i],y[i])

ani = FuncAnimation(fig,animate,frames=len(x),interval = 100,repeat = False)
plt.show()