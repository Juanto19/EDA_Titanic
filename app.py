import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go

def interactive_space(df_plot, grouping_variables=['Survived', 'Group_Age', 'Pclass', 'Embarked', 'Sex', 'deck', 'FamilyID']):
    
    # Título de la app
    st.title('Interactive Titanic Data Visualization')

    # Selección de variables para agrupar
    selected_vars = st.multiselect(
        'Group by:', 
        options=grouping_variables, 
        default=[]
    )
    
    # Generar posiciones de los puntos en un cluster
    def generate_cluster_positions(center_x, center_y, n_points):
        angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
        radii = np.random.uniform(0, 1, size=n_points)
        x_offsets = radii * np.cos(angles)
        y_offsets = radii * np.sin(angles)
        return center_x + x_offsets, center_y + y_offsets

    # Actualizar la gráfica y los conteos
    if selected_vars:
        df_plot['Group'] = df_plot[selected_vars].astype(str).agg('-'.join, axis=1)
    else:
        df_plot['Group'] = 'All Passengers'

    groups = df_plot['Group'].value_counts().index.tolist()
    
    fig = go.Figure()

    group_counts = []

    # Definir parámetros para la disposición en filas y columnas
    max_clusters_per_row = 5
    row_height = 5  # Espacio vertical entre filas
    cluster_spacing_x = 5  # Espacio horizontal entre clusters

    max_row = len(groups) // max_clusters_per_row
    # Generar un cluster para cada grupo
    for i, group in enumerate(groups):
        
        group_df_plot = df_plot[df_plot['Group'] == group]
        n_points = len(group_df_plot)
        
        per_points = round((n_points / len(df_plot)) * 100, 2)

        # Calcular el centro del cluster basado en la fila y la columna
        row = i // max_clusters_per_row  # Definir la fila (empezando por 0)
        col = i % max_clusters_per_row   # Definir la columna (de 0 a max_clusters_per_row-1)

        center_x = col * cluster_spacing_x  # Separar los clusters en la fila
        center_y = -row * row_height        # Cada fila tendrá una altura diferente
        
        #definir la distancia de las etiquetas de grupo y numero de individuos en funcion de la fila
        if row == 0:
            pos = 1.3
        elif row == 1:
            pos = 1.8
        elif row == 2:
            pos = 2.5
        elif row == 3:
            pos = 3
        elif row == 4:
            pos = 3.5
        else:
            pos = 4

        # Generar posiciones para los puntos del cluster
        x_positions, y_positions = generate_cluster_positions(center_x, center_y, n_points)

        # Obtener información para el hover
        hover_data = group_df_plot[['Name', 'Survived', 'Sex', 'Age', 'Fare', 'Pclass', 'Embarked', 'deck', 'n_fam', 'FamilyID', 'Family_Survival_Rate']].to_dict('records')
        hover_text = [
            f"Name: {d['Name']}<br>Survived: {d['Survived']}<br>Sex: {d['Sex']}<br>Age: {d['Age']}<br>Fare: {d['Fare']}<br>Pclass: {d['Pclass']}<br>Embarked: {d['Embarked']}<br>Deck: {d['deck']}<br>n_fam: {d['n_fam']}<br>FamilyID: {d['FamilyID']}<br>Family Survival Rate: {d['Family_Survival_Rate']}"
            for d in hover_data
        ]
        fig.add_trace(go.Scatter(
            x=x_positions,
            y=y_positions,
            mode='markers',
            marker=dict(size=4),
            name=group,
            text=hover_text,
            hoverinfo='text'
        ))

        # Añadir el número de individuos en cada grupo
        fig.add_trace(go.Scatter(
            x=[center_x],
            y=[center_y - (0.2 + pos)],            # Posicionar el texto debajo del cluster
            text=[f'{n_points} ({per_points}%) <br>{group}'],  
            mode='text',
            textfont=dict(color='black', size=12-(pos*0.7)),  # Usar el color blanco para el texto
            showlegend=True, 
             name=f'{n_points}'  # Hacer que el texto sea visible solo cuando el grupo es visible
        ))

        # Ajustar diseño de la gráfica
        fig.update_layout(
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        title={
            'text': 'Interactive Categorical Grouping of Titanic Passengers',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        legend_title='Group',
        template='plotly_white'  # Set the theme here
        )


    if selected_vars == []:
        label = 'Index'
    else:
        label = ' + '.join(selected_vars)

    # Ajustar diseño de la gráfica
    fig.update_layout(
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        title='Interactive Categorical Grouping of Titanic Passengers',
        legend_title=f'{label}',
    )

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig)

# Ejemplo de uso
if __name__ == '__main__':
    df_plot = pd.read_csv(r'data\titanic_clean.csv')  # Asegúrate de cargar tu DataFrame aquí
    interactive_space(df_plot)