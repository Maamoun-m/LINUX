# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 01:25:39 2023

@author: mekki
"""
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Read data from text file into pandas DataFrame
df = pd.read_csv('data.txt', delimiter=' ', header=None, names=['date', 'value'])
df['date'] = pd.to_datetime(df['date'])

# Create Dash app and layout
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Nikkei Index'),
    dcc.Graph(
        id='time-series',
        figure=px.line(df, x='date', y='value', title='Nikkei Index Time Series')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

