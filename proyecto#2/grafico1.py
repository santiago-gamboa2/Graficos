import pandas as pd
import matplotlib.pyplot as plt

data = {
    'id': list(range(1, 21)),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.boxplot([df[df['materia'] == 'Matemáticas']['nota'],
             df[df['materia'] == 'Historia']['nota'],
             df[df['materia'] == 'Ciencias']['nota'],
             df[df['materia'] == 'Lenguaje']['nota']], labels=['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'])
plt.xlabel('Materia')
plt.ylabel('Notas')
plt.title('Distribución de Notas de Estudiantes por Materia')
plt.show()
