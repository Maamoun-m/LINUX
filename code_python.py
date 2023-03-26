
"""
Created on Sun Mar 20 17:09:06 2023

@author: mekki
"""
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

df = pd.read_csv('arbitrum_prices.csv')

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Arbitrum Prices'),
    dcc.Graph(id='arbitrum-graph'),
    dcc.Interval(
        id='interval-component',
        interval=60*1000,
        n_intervals=0
    )
])
@app.callback(Output('arbitrum-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph(n):
    current_time = pd.Timestamp.now()
    filtered_df = df[df['TIME'] <= current_time]
    trace = go.Scatter(x=filtered_df['TIME'], y=filtered_df['PRIX'])
    layout = go.Layout(title='Arbitrum prices Over Time',
                       xaxis=dict(title='Time'),
                       yaxis=dict(title='Price'))
    return {'data': [trace], 'layout': layout}

if __name__ == '__main__':
    app.run_server(host = '0.0.0.0',port = 8000, debug=True)
