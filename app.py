import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go

def interactive_space(df_plot, grouping_variables=['Survived', 'Age', 'Pclass', 'Embarked', 'Sex', 'deck', 'FamilyID']):
    
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

    # Definir parámetros para la disposición en filas y columnas
    max_clusters_per_row = 5
    row_height = 5
    cluster_spacing_x = 5

    max_row = len(groups) // max_clusters_per_row
    # Generar un cluster para cada grupo
    for i, group in enumerate(groups):
        
        group_df_plot = df_plot[df_plot['Group'] == group]
        n_points = len(group_df_plot)
        
        row = i // max_clusters_per_row
        col = i % max_clusters_per_row

        center_x = col * cluster_spacing_x
        center_y = -row * row_height

        x_positions, y_positions = generate_cluster_positions(center_x, center_y, n_points)

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
            y=[center_y - 0.2],
            text=[f'{n_points}<br>{group}'],
            mode='text',
            textfont=dict(color='black', size=12),
            showlegend=False
        ))

    # Configurar layout del gráfico
    fig.update_layout(
        title='Interactive Categorical Grouping of Titanic Passengers',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        template='plotly_white'
    )

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig)

# Ejemplo de uso
if __name__ == '__main__':
    df_plot = pd.read_csv('titanic_clean.csv')  # Asegúrate de cargar tu DataFrame aquí
    interactive_space(df_plot)