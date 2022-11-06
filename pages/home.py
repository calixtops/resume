import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=0)

# resume sample template from https://zety.com/
layout = html.Div([




    dcc.Markdown('# Pedro Silveira Calixto', style={'textAlign':'center'}),

    html.Div([

    html.Div([

    html.A([
    html.Img(
        src='https://cdn-icons-png.flaticon.com/512/1051/1051377.png?w=360',
        style={
            'height' : '4%',
            'width' : '4%',
        })
    ], href='https://github.com/calixtops', style = {'height':'5%'}),



    html.A([
    html.Img(
        src='https://cdn-icons-png.flaticon.com/512/174/174857.png',
        style={
            'height' : '4%',
            'width' : '4%',
        })
    ], href='https://www.linkedin.com/in/calixtops/', style = {'height':'5%',"margin-left": "15px"}),

    ] , className = 'col-6', style = {'float':'right'}),

    html.Br(),
    html.Br(),


    ],className = 'row-2',style = {'float':'center'}),




    dcc.Markdown('### Resumo Profissional', style={'textAlign': 'center'}),



    html.Hr(),

    dcc.Markdown('Oceanógrafo com ampla experiência em projetos de apoio à pesquisa e desenvolvimento. Sou mestre em ciências pela \n'
                 'Universidade de São Paulo e possuo experiência em análise de dados meteoceanográficos, modelos e dados observacionais. \n'
                 'Possuo dois anos de experiência docente pela Universidade Federal do Ceará, como professor, lecionei disciplinas \n'
                 'relacionadas à análise e apresentação de dados oceanográficos e dinâmica de fluídos. Atualmente colaboro com o \n'
                 'Programa Cientista Chefe Meio Ambiente (SEMA-CE), aonde está sendo desenvolvido a Plataforma Estadual de Dados Ambientais (PEDEA).  \n'
                 'Experiência na execução de modelos de Machine Learning e manipulação de dados em Python.',
                 style={'textAlign': 'center', 'white-space': 'pre'}),

    dcc.Markdown('### Competências', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Data Science
            * Python
            * Machine Learning
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            * Pandas / Seaborn / Matplotlib / Dash / Plotly 
            * QGIS
            ''')
        ], width=3),

        dbc.Col([
            dcc.Markdown('''
            * Matlab
            * SQL
            * R
            ''')
        ], width=3)


    ], justify='center'),

    dcc.Markdown('### Experiência Profissional', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('03/2021 - Presente', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Pesquisador / Profissional SIG** \n'
                         '*Programa Cientista Chefe Meio Ambiente* \n'
                         '*Secretaria do Meio Ambiente - Fortaleza, Ceará*',
                         style={'white-space': 'pre'},
                         className='ms-3'),


            dcc.Markdown('Projeto financiado pela Fundação Cearense de Apoio ao Desenvolvimento Científico e Tecnológico (FUNCAP). \n'
                        'Visa articular a pesquisa científica com demandas da gestão pública em benefício da sociedade.',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Elaboração de documento com normas e padrões para a produção e armazenamento de dados georeferenciados e metadados.'),
                html.Li('Aquisição e padronização de dados ambientais de vários pontos focais no Estado.'),
                html.Li('Criação de um banco de dados (PostGIS) e apresentação através da Plataforma Estadual '
                        'de Dados Ambientais (https://pedea.sema.ce.gov.br/portal/).'),
                html.Li('Ferramentas utilizadas: QGIS / Python / Dash / SQL')
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('06/2021 - 06/2022',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**CEO** \n'
                         '*SIARA Tecnologia e Consultoria Ambiental*',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            dcc.Markdown('Constituição de uma start-up de tecnologia ambiental, promovido pelo programa Clusters \n'
                         'de Inovação Econômica e Corredores Digitais.',
                         style={'white-space': 'pre'},
                         className='ms-3'),

            html.Ul([
                html.Li(
                    'Projeto relacionado à energia eólica e a falta de soluções preditivas para programar a manutenção periódica dos equipamentos.'),
                html.Li(
                    'Desenvolvimento de uma aplicação em Flutter alimentada por uma API meteorológica e análise usando inteligência artificial '
                     'para ajudar a planejar a manutenção obrigatória de equipamentos.'),
                html.Li(
                    'Ferramentas utilizadas: Flutter / Python'),
            ])
        ], width=5)
    ], justify='center'),



        dbc.Row([
        dbc.Col([
            dcc.Markdown('03/2019 - 03/2021', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Professor Substituto da Carreira do Magistério Superior** \n'
                         '*Instituto de Ciências do Mar, Universidade Federal do Ceará* \n',
                         style={'white-space': 'pre'},
                         className='ms-3'),


            dcc.Markdown('Componentes curriculares ministradas para os cursos de graduação em Oceanografia e Ciências Ambientais:',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Análise e Apresentação de Dados Oceanográficos em Python'),
                html.Li('Interação Oceano-Atmosfera.'),
                html.Li('Oceanografia Física Descritiva '),
                html.Li('Oceanografia Dinâmica I')
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('02/2017 - 02/2019',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Pesquisador** \n'
                         '*Fundação Cearense de Meteorologia e Recursos hídricos (FUNCEME)*',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            dcc.Markdown('Assistência técnica e científica em projetos de pesquisa e desenvolvimento relacionados \n'
                         'ao tempo e clima, com foco nos recursos hídricos do Estado do Ceará.',
                         style={'white-space': 'pre'},
                         className='ms-3'),

            html.Ul([
                html.Li(
                    'Aquisição, processamento e apresentação de dados meteorológicos e oceanográficos.'),
                html.Li(
                    'Ferramentas utilizadas: Python (Seaborn, Matplotlib, Pandas, ggplot2) / Matlab / Fortran'),
            ])
        ], width=5)
    ], justify='center'),


    dbc.Row([
        dbc.Col([
            dcc.Markdown('2015 - 2016',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Pesquisador Colaborador** \n'
                         '*Petróleo Brasileiro S.A - Petrobras*',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            dcc.Markdown('Utilização de dados observacionais e modelos para a caracterização física da \n'
                        'plataforma continental e região oceânica proxima aos estados do Espirito Santo e \n'
                        'Sergipe-Alagoas, Brasil.',
                         style={'white-space': 'pre'},
                         className='ms-3'),

            html.Ul([
                html.Li(
                    'Caracterização da Circulação e das Massas de Água na Bacia do Espírito Santo- AMBES'),
                html.Li(
                    'Caracterização da Circulação e das Massas de Água na Bacia Sergipe-Alagoas - SEAL'),
            ])
        ], width=5)
    ], justify='center'),


    dcc.Markdown('### Educação', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2016',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Mestrado em Ciência**s\n'
                         '*Universidade de São Paulo - São Paulo, SP*',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),


    dbc.Row([
        dbc.Col([
            dcc.Markdown('2014',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Graduação em Oceanografia** \n'
                         '*Universidade Federal do Ceará - Fortaleza, CE*',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),



])
