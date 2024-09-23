import pandas as pd
import plotly.express as px
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
    fig_pie = px.pie(
        top_towns,
        names='Town',
        values='Percentage of Education level of residents-university',
        hole=0.3,
        title=f"Top {num_towns} Towns by University-Level Education Percentage",
        labels={'Percentage of Education level of residents-university': 'University Education'}
    )

    # Update layout for pie chart
    fig_pie.update_layout(
        title={
            'font_size': 24,
            'font_family': "Arial"
        },
        legend_title='Town',
        legend=dict(
            x=1.05,
            y=0.5,
            traceorder='normal',
            orientation='v'
        ),
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
    fig_heatmap = px.imshow(
        correlation_matrix,
        color_continuous_scale=color_scale,
        text_auto=True,
        title='Correlation Matrix Heatmap'
    )

    # Update the layout for heatmap
    fig_heatmap.update_layout(
        title='Correlation Matrix Heatmap',
        xaxis_title='Variables',
        yaxis_title='Variables',
        xaxis=dict(tickangle=-45),
        yaxis=dict(tickangle=0),
        autosize=False,  # Disable autosize to use explicit dimensions
        width=800,       # Width of the heatmap
        height=800       # Height of the heatmap
    )

    # Display the heatmap
    st.title('Correlation Matrix Heatmap')
    st.plotly_chart(fig_heatmap)



























    
