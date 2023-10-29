import numpy as np
import matplotlib.pyplot as plt

# Datos de calificaciones de los estudiantes
matematicas = np.random.default_rng(42).integers(50, 100, 20)
ciencias = np.random.default_rng(42).integers(40, 95, 20)
literatura = np.random.default_rng(42).integers(60, 100, 20)

# Calificaciones promedio y errores
promedio_matematicas = np.mean(matematicas)
promedio_ciencias = np.mean(ciencias)
promedio_literatura = np.mean(literatura)

std_matematicas = np.std(matematicas)
std_ciencias = np.std(ciencias)
std_literatura = np.std(literatura)

materias = ['Matemáticas', 'Ciencias', 'Literatura']
promedios = [promedio_matematicas, promedio_ciencias, promedio_literatura]
errores = [std_matematicas, std_ciencias, std_literatura]

# Crear el gráfico de barras de error
plt.figure(figsize=(6, 4))  # Tamaño más angosto
plt.bar(materias, promedios, yerr=errores, color='lightblue', alpha=0.7, capsize=5)

# Etiquetas de los ejes
plt.xlabel('Materias')
plt.ylabel('Calificaciones Promedio')
plt.title('Calificaciones Promedio con Barras de Error')

# Estilo visual
plt.xticks(rotation=0)  # Alinea las etiquetas de las materias horizontalmente
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Eliminar el fondo
plt.gca().set_facecolor('white')

# Mostrar el gráfico
plt.tight_layout()  # Ajusta el espacio
plt.show()
