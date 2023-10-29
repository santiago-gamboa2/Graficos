import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)

plt.figure(figsize=(8, 6))
plt.scatter(matematicas, ciencias, c='b', marker='o', label='Calificaciones')

plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Calificaciones de Ciencias')

plt.title('Relación entre Calificaciones de Matemáticas y Ciencias')

plt.legend()

plt.grid(True)
plt.show()
