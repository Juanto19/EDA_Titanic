import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Available grouping variables
grouping_variables = ['Survived', 'Age', 'Pclass', 'Embarked', 'Sex', 'deck', 'FamilyID']

# Load your Titanic dataset
df_plot = pd.read_csv('titanic_clean.csv')  # Use your actual data

# Define the app layout
st.title('Interactive Titanic Data Visualization')

# Dropdown for grouping
selected_vars = st.multiselect('Select variables to group by:', grouping_variables)

# Generate positions for the clusters
def generate_cluster_positions(center_x, center_y, n_points):
    angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    radii = np.random.uniform(0, 1, size=n_points)  
    x_offsets = radii * np.cos(angles)
    y_offsets = radii * np.sin(angles)
    return center_x + x_offsets, center_y + y_offsets

# Plot the scatterplot
if selected_vars:
    df_plot['Group'] = df_plot[selected_vars].astype(str).agg('-'.join, axis=1)
else:
    df_plot['Group'] = 'All Passengers'

groups = df_plot['Group'].value_counts().index.tolist()

# Initialize figure
fig = go.Figure()

for i, group in enumerate(groups):
    group_df_plot = df_plot[df_plot['Group'] == group]
    n_points = len(group_df_plot)

    center_x, center_y = i * 5, 0
    x_positions, y_positions = generate_cluster_positions(center_x, center_y, n_points)

    hover_data = group_df_plot[['Name', 'Survived', 'Sex', 'Age', 'Fare', 'Pclass', 'Embarked', 'deck', 'FamilyID']].to_dict('records')
    hover_text = [
        f"Name: {d['Name']}<br>Survived: {d['Survived']}<br>Sex: {d['Sex']}<br>Age: {d['Age']}<br>Fare: {d['Fare']}<br>Pclass: {d['Pclass']}<br>Embarked: {d['Embarked']}"
        for d in hover_data
    ]

    fig.add_trace(go.Scatter(
        x=x_positions,
        y=y_positions,
        mode='markers',
        marker=dict(size=5),
        name=group,
        text=hover_text,
        hoverinfo='text'
    ))

# Update the layout of the figure
fig.update_layout(
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    title='Categorical Grouping of Titanic Passengers',
    showlegend=False
)

# Display the plot
st.plotly_chart(fig)
