import numpy as np
import matplotlib.pyplot as plt

matematicas = np.random.default_rng(42).integers(50, 100, 20)

plt.figure(figsize=(8, 6))
plt.hist(matematicas, bins=10, color='lightpurple', edgecolor='black')

plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Frecuencia')
plt.title('Distribución de Calificaciones de Matemáticas')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
