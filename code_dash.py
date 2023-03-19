# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 01:25:39 2023

@author: mekki
"""
import subprocess
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# retrieve initial data
index_value = subprocess.check_output(["curl", "https://www.marketwatch.com/investing/index/nik/charts?countryCode=JP", "|", "grep", "'<bg-quote class=\"value'>\"'", "|", "sed", "'s/<bg-quote class=\"value\">//g'", "|", "sed", "'s/<\\/bg-quote>//g'", "|", "awk", "'{print $1}'"]).decode("utf-8").strip()

# create the app
app = dash.Dash(__name__)

# define the layout
app.layout = html.Div([
    html.H1("Nikkei Index"),
    html.Div(id="index-value", children=f"Current value: {index_value}"),
    dcc.Interval(id="interval-component", interval=60*1000, n_intervals=0)
])

# define the callbacks
@app.callback(Output("index-value", "children"),
              Input("interval-component", "n_intervals"))
def update_index_value(n):
    index_value = subprocess.check_output(["curl", "https://www.marketwatch.com/investing/index/nik/charts?countryCode=JP", "|", "grep", "'<bg-quote class=\"value'>\"'", "|", "sed", "'s/<bg-quote class=\"value\">//g'", "|", "sed", "'s/<\\/bg-quote>//g'", "|", "awk", "'{print $1}'"]).decode("utf-8").strip()
    return f"Current value: {index_value}"

# run the app
if __name__ == "__main__":
    app.run_server(debug=True)
