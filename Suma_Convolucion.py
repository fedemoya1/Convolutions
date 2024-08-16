import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-4, 10, 50)

f = np.heaviside(t, 1) - np.heaviside(t-3, 1)

g = t*np.heaviside(t, 1) - t*np.heaviside(t-5, 1)
#g = np.where(t<5, t*np.heaviside(t, 1) ,0)

convolucion = np.convolve(f, g, mode="same")/sum(g)
# Gráfica de los resultados
#Tamaño de la figura
plt.figure(figsize=(10, 6))

#Seteamos en qué índice se va a graficar cada función
plt.subplot(3, 1, 1)
plt.stem(t, f)
plt.title('f = u(t) - u(t-3)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(t, g)
plt.title('g = t*u(t) - t*u(t-5); t<=5')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(t+3, convolucion)
plt.title('Convolución: {f*g}')
plt.grid(True)

plt.tight_layout()
plt.savefig('Funciones Exponenciales en tiempo Discreto.png')
plt.show()