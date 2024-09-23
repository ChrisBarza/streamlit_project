import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title='Education Levels Dashboard', layout='wide')

# Define the relative path to the CSV file
file_path = os.path.join(os.path.dirname(__file__), 'Education level copy.csv')

# Check if the file exists
if not os.path.isfile(file_path):
    st.error(f"File not found: {file_path}")
else:
    # Load the CSV file
    education_data = pd.read_csv(file_path)

    # Sidebar for user input
    st.sidebar.header('Filter Options')

    # Dropdown for selecting the number of top towns
    num_towns = st.sidebar.selectbox(
        'Number of Top Towns to Display',
        options=[5, 10, 15],
        index=1  # Default to showing top 10
    )

    # Filter and sort data for pie chart
    filtered_data = education_data[['Town', 'Percentage of Education level of residents-university']]
    top_towns = filtered_data.sort_values(by='Percentage of Education level of residents-university', ascending=False).head(num_towns)

    # Create the interactive pie chart
    fig_pie = go.Figure(data=[go.Pie(
        labels=top_towns['Town'],
        values=top_towns['Percentage of Education level of residents-university'],
        hole=0.3,
        textinfo='label+percent',
        hoverinfo='label+percent+value',
        pull=[0.1] * len(top_towns)
    )])

    # Update layout for pie chart
    fig_pie.update_layout(
        title={
            'text': f"Top {num_towns} Towns by University-Level Education Percentage",
            'font_size': 24,
            'font_family': "Arial",
            'x': 0.5,
            'xanchor': 'center'
        },
        legend_title='Town',
        legend=dict(
            x=1.05,
            y=0.5,
            traceorder='normal',
            orientation='v'
        ),
        annotations=[dict(
            text='University\nEducation',
            x=0.5,
            y=0.5,
            font_size=20,
            showarrow=False
        )],
        margin=dict(t=100, b=0, l=0, r=0)
    )

    # Display the pie chart
    st.title('Top Towns by University-Level Education Percentage')
    st.plotly_chart(fig_pie, use_container_width=True)

    # Select only numeric columns for heatmap
    numeric_data = education_data.select_dtypes(include=['number'])

    # Calculate the correlation matrix
    correlation_matrix = numeric_data.corr()

    # Sidebar for selecting color scale
    color_scale = st.sidebar.selectbox(
        'Choose a color scale:',
        ['RdBu', 'Viridis', 'Cividis', 'Blues', 'Greens']
    )

    # Sidebar slider for precision
    precision = st.sidebar.slider(
        'Select the number of decimal places for annotations:',
        min_value=0, max_value=4, value=2
    )

    # Create the heatmap with annotations
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        colorscale=color_scale,
        colorbar=dict(title='Correlation'),
        zmin=-1,
        zmax=1,
        text=correlation_matrix.round(precision).astype(str),
        texttemplate='%{text}',
        textfont=dict(size=12, color='black'),
        hoverinfo='text',
        showscale=True
    ))

    # Update the layout for heatmap
    fig_heatmap.update_layout(
        title='Correlation Matrix Heatmap',
        xaxis_title='Variables',
        yaxis_title='Variables',
        xaxis=dict(tickangle=-45),
        yaxis=dict(tickangle=0)
    )

    # Display the heatmap
    st.title('Correlation Matrix Heatmap')
    st.plotly_chart(fig_heatmap)

























    
