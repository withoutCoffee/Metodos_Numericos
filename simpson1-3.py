import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 0.6, 1.2, 1.8, 2.4, 4.2])
y = np.array([8, 9, 8, 6, 3, 0])

h  = (x[-1] - x[0])/(len(x)-1)

# simpsom 1/3
s = 0
for i in range(1,len(x)-1):
  if i%2 == 0:
    s = s + 2*y[i]
  else:
    s = s + 4*y[i]
s = (h/3)*(s + y[0] + y[-1])

plt.plot(x,y,color='orange',label="pontos")
plt.title(f"Simpson 1/3 - > H={h}")
plt.fill_between(x,0,y,alpha=0.5,label=f'Soma={s}')
plt.legend()
plt.show()