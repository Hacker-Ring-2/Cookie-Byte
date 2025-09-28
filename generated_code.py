
import plotly.graph_objects as go

# Data
labels = ['Food', 'Rent', 'Travel', 'Savings']
values = [40.0, 30.0, 20.0, 10.0]

# Create pie chart
fig = go.Figure(data=[go.Pie(
    labels=labels, 
    values=values,
    hole=0.3,
    textinfo='label+percent',
    insidetextorientation='radial'
)])

# Update layout
fig.update_layout(
    title='expenses (Food=40',
    height=500,
    width=700
)

# The figure object will be returned
