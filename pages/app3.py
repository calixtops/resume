import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar
import numpy as np
import gc

dash.register_page(__name__)


def layout():
    return html.Div([dcc.Markdown('Teste')])
