import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar
import numpy as np
import gc

dash.register_page(__name__)

df = pd.read_csv('assets/DadosDesafioCientista_full.csv')


mensagem = 'Para exportar a tabela, clique no botão "export" abaixo:'
msg_plot = 'Utilize o slider para escolher o número de bairros a incluir no gráfico.'

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    

                html.Div([


                        html.Div([
                            html.H2('Faturamento e Potencial para os bairros do Rio de Janeiro e São Paulo'),
                            html.H4('Projeto de Machine Learning para estimar o faturamento dos bairros de SP com base \n'
                                    'no faturamento dos bairros do RJ'
                                ),
                            ],
                            className='row',
                            style = {'padding-top' : '1%'}
                        ),


                        ],
                        className = 'row',
                        style = {'height' : '10%',
                                'background-color' : '#e0e0eb',
                                'border-radius': 10}
                        ),


                html.Hr(),
                html.H5('Clique no link para acessar o app completo:'),
                dcc.Link(html.A('https://dash-case1.uc.r.appspot.com/'), 
                    href='https://dash-case1.uc.r.appspot.com/', 
                    style={'color': 'blue', 'text-decoration': 'none'},refresh = True),
                html.P('Escolha qual cidade você deseja analisar:'),
                dcc.Dropdown(id='city-choice',
                             options=[{'label':x, 'value':x}
                                      for x in sorted(df.cidade.unique())],
                             value='São Paulo'
                             ),

                html.Div([


                    html.Hr(style={
                    'margin-top':'-2px',
                    'height':'7px',
                    'background-color':'#00cc00',
                    'border':'none',
                    }),
                    html.P(mensagem),   

                dcc.Loading(html.Div([
                    dash_table.DataTable(
                    id='table_app2',
                    columns=[{"name": i.title(), "id": i, "deletable": True} 
                             for i in df.columns],
                    data=[],
                    column_selectable="multi",

                    sort_action='native',
                    sort_mode='single',
                    filter_action='native',
                    style_header=dict(backgroundColor="paleturquoise"),
                    style_data=dict(backgroundColor="lavender",width='auto'),
                    style_cell={'textAlign':'left'},
                    export_format='xlsx',
                    page_action="native",
                    style_table={
                    'maxHeight': '600px',
                    'maxWidth': '1100px',

                    'overflowY': 'scroll',
                    'padding-top' : '1%',

                    },
                    ),
                ])),

                    html.Br(),
                    html.Hr(),
                    html.H3(msg_plot),
                    dcc.Slider(
                        id="bairros",
                        min=1,
                        max=df.shape[0],
                        value=df.shape[0],
                        ),

                    dcc.Loading(dcc.Graph(id='fig_app2'))
                ]),








                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])
suppress_callback_exceptions=True
@callback(
    Output("fig_app2", "figure"), 
    Output("table_app2", "data"), 
    Output("bairros", "max"),

    Input('city-choice','value'),
    Input("bairros", "value"),
    )

def interactive_graphs(value_city,bairros):

    df = pd.read_csv('assets/DadosDesafioCientista_full.csv')

    df = df[df.cidade==value_city]

    df_top = df.sort_values('faturamento',ascending= False).head(bairros)

    fig = px.bar(df_top,
    x='nome',
    y='faturamento',
    color='potencial',
    template='ggplot2',
    hover_data=df_top.columns,
    height=600,
    labels=dict(
        nome="Bairros", 
        faturamento="Faturamento", 
        potencial="Potencial",
        height=500),
    color_discrete_map={
    'Alto': '#8080ff',
    'Médio': '#66ff66',
    'Baixo': '#ff8080'},
    title='Gráfico com os {} bairros de {} que apresentam maior faturamento.'.format(bairros,value_city))

    return fig, df.to_dict('records'), df.shape[0]