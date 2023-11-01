#creo que este grafico quedo mejor que todos xd
import pandas as pd
import plotly.express as px

data = {
    'id': list(range(1, 21)),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

aprobados = df[df['aprobado'] == 'Sí'].shape[0]
no_aprobados = df[df['aprobado'] == 'No'].shape[0]


data_pie = pd.DataFrame({'Aprobados': [aprobados], 'No Aprobados': [no_aprobados]})

fig = px.pie(data_pie, names=data_pie.columns, values=data_pie.iloc[0])

fig.update_traces(textinfo='percent+label')
fig.update_layout(title='Distribución de Aprobados vs. No Aprobados')

fig.show()
