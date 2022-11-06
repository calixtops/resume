import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path = '/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([




    dcc.Markdown('''# Pedro Silveira Calixto''', 
        style={'textAlign':'center','display':'inline'}),


    dcc.Markdown('''[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/calixtops/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/calixtops)''', 
        style={'textAlign':'center','display':'inline'}),


    dcc.Markdown('### Resumo Profissional', style={'textAlign': 'center'}),



    html.Hr(),

    dcc.Markdown(

                '''

                Oceanógrafo com ampla experiência em projetos de apoio à pesquisa e desenvolvimento. 
                Sou mestre em ciências pela Universidade de São Paulo e possuo experiência em análise 
                de dados meteoceanográficos, modelos e dados observacionais. Tive a satisfação de atuar como
                docente pela Universidade Federal do Ceará, aonde lecionei disciplinas relacionadas
                à análise e apresentação de dados oceanográficos e dinâmica de fluidos. Atualmente colaboro 
                com o Programa Cientista Chefe Meio Ambiente (SEMA-CE), onde está sendo desenvolvido a Plataforma 
                Estadual de Dados Ambientais (PEDEA). Experiência na execução de modelos de Machine Learning e manipulação de dados em Python.


                ''',className = 'text-justify', style={'textAlign': 'center'}),

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

            dcc.Markdown(

                '''
            - Elaboração de documento com normas e padrões para a produção e armazenamento de dados georeferenciados e metadados.
            * Aquisição e padronização de dados ambientais de vários pontos focais no Estado.
            * Criação de um banco de dados (PostGIS) e apresentação através da 
            [Plataforma Estadual de Dados Ambientais](https://pedea.sema.ce.gov.br/portal/).
            * Ferramentas utilizadas: QGIS / Python / Dash / SQL


                '''


                ),

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
            dcc.Markdown('''Constituição de uma start-up de tecnologia ambiental, promovido pelo programa \
                [Clusters de Inovação Econômica e Corredores Digitais](https://www.sedet.ce.gov.br/negocios/comercio-servicos-e-inovacao/programa-clusters-economicos-de-inovacao/).''',
                className='ms-3'),

            dcc.Markdown(

                '''

                * Projeto relacionado à energia eólica e a falta de soluções preditivas para programar a manutenção periódica dos equipamentos.
                * Desenvolvimento de uma aplicação em Flutter alimentada por uma API meteorológica e análise usando inteligência artificial 
                para ajudar a planejar a manutenção obrigatória de equipamentos.
                * Ferramentas utilizadas: Flutter / Python
                '''

                )




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

            dcc.Markdown(

                '''
                * Análise e Apresentação de Dados Oceanográficos em Python
                * Interação Oceano-Atmosfera.
                * Oceanografia Física Descritiva 
                * Oceanografia Dinâmica I

                '''

                )

        
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
