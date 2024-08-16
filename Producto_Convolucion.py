import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Definir el dominio del tiempo extendido
t_ext = np.linspace(0, 200, 3000)  # Comienza en 0 y extiende más allá de 100
t = np.linspace(0, 100, 3000)  # Rango original

# Definir las funciones sobre el dominio extendido
f_ext = np.sin(t_ext)
g_ext = np.cos(t_ext)

# Realizar la convolución sobre el dominio extendido
convolucion_ext = np.convolve(f_ext, g_ext, mode='full') / sum(g_ext)  # Usar sum(g_ext) para normalización

# Calcular el rango de tiempo de la convolución
t_conv_ext = np.linspace(t_ext[0] + t_ext[0], t_ext[-1] + t_ext[-1], len(convolucion_ext))

# Recortar la convolución al rango de tiempo original para visualización
# Encuentra los índices del array t_conv_ext que se corresponden con el rango de t
indices = (t_conv_ext >= t[0]) & (t_conv_ext <= t[-1])
t_conv = t_conv_ext[indices]
convolucion = convolucion_ext[indices]

# Gráfica de los resultados
plt.figure(figsize=(12, 6))
plt.plot(t_conv, convolucion, label='Convolución sin(t) * cos(t)')
plt.xlabel('Tiempo t')
plt.ylabel('Respuesta y(t)')
plt.title('Convolución con inicio en cero y extensiones para minimizar efectos de borde')
plt.legend()
plt.grid(True)
plt.show()