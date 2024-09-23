import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Set page configuration
st.set_page_config(page_title='Education Levels Dashboard', layout='wide')  # Set page title and layout

# Load the CSV file
file_path = '/Users/chrisbarza/Desktop/Education level copy.csv'
education_data = pd.read_csv(file_path)

# Sidebar for user input
st.sidebar.header('Filter Options')

# Dropdown for selecting the number of top towns
num_towns = st.sidebar.selectbox(
    'Number of Top Towns to Display',
    options=[5, 10, 15],
    index=1  # Default to showing top 10
)

# Filter and sort data
filtered_data = education_data[['Town', 'Percentage of Education level of residents-university']]
top_towns = filtered_data.sort_values(by='Percentage of Education level of residents-university', ascending=False).head(num_towns)

# Create the interactive pie chart
fig = go.Figure(data=[go.Pie(
    labels=top_towns['Town'],
    values=top_towns['Percentage of Education level of residents-university'],
    hole=0.3,  # Creates a donut chart if you want a hole in the center
    textinfo='label+percent',  # Show both labels and percentages
    hoverinfo='label+percent+value',  # Show more details on hover
    pull=[0.1] * len(top_towns)  # Slightly pull each slice out to make it more interactive (optional)
)])

# Update layout for better interaction and aesthetics
fig.update_layout(
    title={
        'text': f"Top {num_towns} Towns by University-Level Education Percentage",
        'font_size': 24,
        'font_family': "Arial",
        'x': 0.5,  # Center the title
        'xanchor': 'center'
    },
    legend_title='Town',
    legend=dict(
        x=1.05,  # Position the legend outside the chart
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
    margin=dict(t=100, b=0, l=0, r=0)  # Adjust margins for a better layout
)

# Streamlit app
st.title('Top Towns by University-Level Education Percentage')

# Display sidebar content
st.sidebar.write(
    """
    Use the dropdown in the sidebar to select the number of top towns to display in the pie chart.
    The chart will update to show the selected number of towns.
    """
)

# Display the pie chart
st.plotly_chart(fig, use_container_width=True)



import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Load the CSV file
file_path = '/Users/chrisbarza/Desktop/Education level copy.csv'
education_data = pd.read_csv(file_path)

# Select only numeric columns
numeric_data = education_data.select_dtypes(include=['number'])

# Calculate the correlation matrix
correlation_matrix = numeric_data.corr()

# Streamlit sidebar for selecting color scale
color_scale = st.sidebar.selectbox(
    'Choose a color scale:',
    ['RdBu', 'Viridis', 'Cividis', 'Blues', 'Greens']
)

# Streamlit slider for precision
precision = st.sidebar.slider(
    'Select the number of decimal places for annotations:',
    min_value=0, max_value=4, value=2
)

# Create the heatmap with annotations
fig = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale=color_scale,  # Use selected color scale
    colorbar=dict(title='Correlation'),
    zmin=-1,  # Set the min value for the color scale
    zmax=1,   # Set the max value for the color scale
    text=correlation_matrix.round(precision).astype(str),  # Add annotations
    texttemplate='%{text}',  # Use text values as annotations
    textfont=dict(size=12, color='black'),  # Font size and color for annotations
    hoverinfo='text',  # Show detailed info on hover
    showscale=True  # Show the color scale
))

# Update the layout
fig.update_layout(
    title='Correlation Matrix Heatmap',
    xaxis_title='Variables',
    yaxis_title='Variables',
    xaxis=dict(tickangle=-45),  # Rotate x-axis labels
    yaxis=dict(tickangle=0)     # Ensure y-axis labels are horizontal
)

# Streamlit app
st.title('Correlation Matrix Heatmap')
st.plotly_chart(fig)
























    