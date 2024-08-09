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


                Oceanógrafo com experiência em análise e visualização de dados, aliada a uma sólida participação em projetos de ciência e tecnologia. 
                Minha expertise abrange a manipulação avançada de dados em Python e desenvolvimento de relatórios analíticos e dashboards interativos para monitoramento de projetos. 
                Atuei como professor substituto no LABOMAR/UFC, ministrando disciplinas de Análise de Dados Ambientais e Oceanografia Física. 
                Destaco minha contribuição na implementação da Plataforma de Dados Estaduais Ambientais do Ceará, uma IDE crucial para a gestão ambiental do estado. 
                Além disso, integrei a equipe de monitoramento e previsão meteorológica e oceanográfica no projeto OCEANOP da Petrobras, onde prestei suporte às operações offshore e ao setor 
                de óleo e gás. Busco novas oportunidades para aplicar minhas habilidades em oceanografia e análise de dados, contribuindo para o sucesso de projetos inovadores.


                ''',className = 'text-justify', style={'textAlign': 'justify'}),

    dcc.Markdown('### Competências', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Data Science
            * Python
            * Machine Learning
            ''')
        ], width=3),
        dbc.Col([
            dcc.Markdown('''
            * Scikit-Learn / PyTorch  
            * Pandas / Seaborn / Matplotlib  
            * Dash / Plotly  
            ''')
        ], width=3),


        dbc.Col([
            dcc.Markdown('''
            * Html / CSS  
            * JavaScript
            * Dart
            ''')
        ], width=3),


        dbc.Col([
            dcc.Markdown('''
            * Quantum GIS
            * SQL
            * Matlab / R
            ''')
        ], width=3),
        
    ], justify='center'),



    dcc.Markdown('### Experiência Profissional', style={'textAlign': 'center'}),
    html.Hr(),



    dbc.Row([
        dbc.Col([
            dcc.Markdown('03/2023 - 08/2024', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Analista Ambiental** \n'
                         '*Petróleo Brasileiro S.A - Petrobras* \n'
                         '*Cepemar Serviços de Consultoria em Meio Ambiente - Macaé, Rio de Janeiro*',
                         style={'white-space': 'pre'},
                         ),


            dcc.Markdown('Experiência como membro da equipe de monitoramento e previsão meteorológica e oceanográfica no projeto OCEANOP (Oceanografia Operacional) da Petrobras. \n'
                          '  Principais contribuições incluem:',
                         ),

            dcc.Markdown(

                '''
            * Elaboração de relatórios: Criação de relatórios técnicos para diversas finalidades, incluindo planejamento de operações, estudos de impacto e suporte a investigação de incidentes.
            * Análise de dados: Análise detalhada de dados oceanográficos para suporte a operações offshore e modelagem de dispersão de óleo.
            * Desenvolvimento de produtos: Criação de produtos especializados, como boletins e simulações, para atender às necessidades específicas do setor.
            * Apoio a operações: Fornecimento de informações meteorológicas e oceanográficas em tempo real para otimizar operações offshore e garantir a segurança das equipes.
            * Ferramentas utilizadas:  Python / QGIS / SQL


                '''




                ),

        ], width=5)
    ], justify='center'),




    dbc.Row([
        dbc.Col([
            dcc.Markdown('03/2021 - Presente', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Pesquisador / Profissional SIG** \n'
                         '*Programa Cientista Chefe Meio Ambiente* \n'
                         '*Secretaria do Meio Ambiente - Fortaleza, Ceará*',
                         style={'white-space': 'pre'},
                         ),


            dcc.Markdown('Projeto financiado pela Fundação Cearense de Apoio ao Desenvolvimento Científico e Tecnológico (FUNCAP). \n'
                        'Visa articular a pesquisa científica com demandas da gestão pública em benefício da sociedade.',
                         ),

            dcc.Markdown(

                '''
            * Elaboração de documento com normas e padrões para a produção e armazenamento de dados georeferenciados e metadados.
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
                         ),
            dcc.Markdown('''Constituição de uma start-up de tecnologia ambiental, promovido pelo Programa \
                [Clusters Econômicos de Inovação](https://www.sct.ce.gov.br/corredoresdigitais/).''',
                ),

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
                         ),


            dcc.Markdown('Componentes curriculares ministradas para os cursos de graduação em Oceanografia e Ciências Ambientais:',
                          ),

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
                         ),
            dcc.Markdown('Assistência técnica e científica em projetos de pesquisa e desenvolvimento relacionados \n'
                         'ao tempo e clima, com foco nos recursos hídricos do Estado do Ceará.',
                         ),

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
                         ),
            dcc.Markdown('Utilização de dados observacionais e modelos para a caracterização física da \n'
                        'plataforma continental e região oceânica proxima aos estados do Espirito Santo e \n'
                        'Sergipe-Alagoas, Brasil.',
                         ),

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
            dcc.Markdown('**Mestrado em Ciências**\n'
                         '*Universidade de São Paulo - São Paulo, SP*',
                         style={'white-space': 'pre'},
                         ),
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
                         ),
        ], width=5)
    ], justify='center'),


    dcc.Markdown('### Cursos', style={'textAlign': 'center'}),
    html.Hr(),


dbc.Accordion([

  dbc.AccordionItem([


    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2022 

                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),

        dbc.Col([
            
            dcc.Markdown(

                        '![Udemy](https://img.shields.io/badge/Udemy-A435F0?style=for-the-badge&logo=Udemy&logoColor=white) \n'


                        '**Machine Learning A-Z™: Hands-On Python & R In Data Science** \n'
                        '[Credential ID UC-14cd6c98-1044-4cb2-891d-32f72d442a58](https://www.udemy.com/certificate/UC-14cd6c98-1044-4cb2-891d-32f72d442a58/)',
                        style={'white-space': 'pre'}
                        ),
        ], width=5)
    ], justify='center'),


    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2022 


                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),

        dbc.Col([
            
            dcc.Markdown(


                        '![Udemy](https://img.shields.io/badge/Udemy-A435F0?style=for-the-badge&logo=Udemy&logoColor=white) \n'


                        '**Looker Studio (Google Data Studio)** \n'
                        '[Credential ID UC-84cbb1e6-cae0-44b4-bc53-8959d5fc560f](https://www.udemy.com/certificate/UC-84cbb1e6-cae0-44b4-bc53-8959d5fc560f/)'

                        ,style={'white-space': 'pre'}),
        ], width=5)
    ], justify='center'),



    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2022 



                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),

        dbc.Col([
            
            dcc.Markdown(
                        '![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NS41MiIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDc1LjUyIDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iNzUuNTIiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDFFNDUiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI3NS41MiIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiMzODlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuMDAgMjJMMTMuNDYgMjJMMTYuNjggMTMuNDdMMTguMDEgMTMuNDdMMjEuMjQgMjJMMTkuNjkgMjJMMTguOTkgMjAuMDFMMTUuNjkgMjAuMDFMMTUuMDAgMjJaTTE3LjM0IDE1LjI4TDE2LjEwIDE4LjgyTDE4LjU4IDE4LjgyTDE3LjM0IDE1LjI4Wk0zMC41NSAyMkwyNS4xOSAyMkwyNS4xOSAxMy40N0wyNi42NyAxMy40N0wyNi42NyAyMC44MkwzMC41NSAyMC44MkwzMC41NSAyMlpNMzQuNTQgMTkuMTZMMzQuNTQgMTkuMTZMMzQuNTQgMTMuNDdMMzYuMDEgMTMuNDdMMzYuMDEgMTkuMThRMzYuMDEgMjAuMDMgMzYuNDUgMjAuNDhRMzYuODggMjAuOTMgMzcuNzMgMjAuOTNMMzcuNzMgMjAuOTNRMzkuNDQgMjAuOTMgMzkuNDQgMTkuMTNMMzkuNDQgMTkuMTNMMzkuNDQgMTMuNDdMNDAuOTEgMTMuNDdMNDAuOTEgMTkuMTdRNDAuOTEgMjAuNTMgNDAuMDQgMjEuMzJRMzkuMTcgMjIuMTIgMzcuNzMgMjIuMTJMMzcuNzMgMjIuMTJRMzYuMjYgMjIuMTIgMzUuNDAgMjEuMzNRMzQuNTQgMjAuNTUgMzQuNTQgMTkuMTZaTTQ2Ljk3IDIyTDQ1LjQ4IDIyTDQ1LjQ4IDEzLjQ3TDQ4LjQ4IDEzLjQ3UTQ5Ljk2IDEzLjQ3IDUwLjc2IDE0LjEzUTUxLjU2IDE0Ljc5IDUxLjU2IDE2LjA1TDUxLjU2IDE2LjA1UTUxLjU2IDE2LjkwIDUxLjE1IDE3LjQ4UTUwLjc0IDE4LjA2IDUwLjAwIDE4LjM3TDUwLjAwIDE4LjM3TDUxLjkyIDIxLjkyTDUxLjkyIDIyTDUwLjMzIDIyTDQ4LjYyIDE4LjcxTDQ2Ljk3IDE4LjcxTDQ2Ljk3IDIyWk00Ni45NyAxNC42Nkw0Ni45NyAxNy41Mkw0OC40OSAxNy41MlE0OS4yNCAxNy41MiA0OS42NiAxNy4xNVE1MC4wOCAxNi43NyA1MC4wOCAxNi4xMUw1MC4wOCAxNi4xMVE1MC4wOCAxNS40MyA0OS42OSAxNS4wNVE0OS4zMCAxNC42OCA0OC41MyAxNC42Nkw0OC41MyAxNC42Nkw0Ni45NyAxNC42NlpNNTYuNzQgMjJMNTUuMjAgMjJMNTguNDIgMTMuNDdMNTkuNzUgMTMuNDdMNjIuOTggMjJMNjEuNDMgMjJMNjAuNzMgMjAuMDFMNTcuNDMgMjAuMDFMNTYuNzQgMjJaTTU5LjA4IDE1LjI4TDU3Ljg1IDE4LjgyTDYwLjMyIDE4LjgyTDU5LjA4IDE1LjI4WiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iI0ZGRkZGRiIgeD0iODguNTIiLz48L3N2Zz4=) \n'
                        

                        '**Machine Learning: classificação com SKLearn** \n'
                        '[Credential ID bf57632f-1780-4952-95fc-1d1c103e88b9](https://cursos.alura.com.br/certificate/bf57632f-1780-4952-95fc-1d1c103e88b9)'

                        ,style={'white-space': 'pre'}),
        ], width=5)
    ], justify='center'),



    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2022 



                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),


        dbc.Col([
            
            dcc.Markdown(
                        '![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NS41MiIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDc1LjUyIDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iNzUuNTIiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDFFNDUiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI3NS41MiIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiMzODlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuMDAgMjJMMTMuNDYgMjJMMTYuNjggMTMuNDdMMTguMDEgMTMuNDdMMjEuMjQgMjJMMTkuNjkgMjJMMTguOTkgMjAuMDFMMTUuNjkgMjAuMDFMMTUuMDAgMjJaTTE3LjM0IDE1LjI4TDE2LjEwIDE4LjgyTDE4LjU4IDE4LjgyTDE3LjM0IDE1LjI4Wk0zMC41NSAyMkwyNS4xOSAyMkwyNS4xOSAxMy40N0wyNi42NyAxMy40N0wyNi42NyAyMC44MkwzMC41NSAyMC44MkwzMC41NSAyMlpNMzQuNTQgMTkuMTZMMzQuNTQgMTkuMTZMMzQuNTQgMTMuNDdMMzYuMDEgMTMuNDdMMzYuMDEgMTkuMThRMzYuMDEgMjAuMDMgMzYuNDUgMjAuNDhRMzYuODggMjAuOTMgMzcuNzMgMjAuOTNMMzcuNzMgMjAuOTNRMzkuNDQgMjAuOTMgMzkuNDQgMTkuMTNMMzkuNDQgMTkuMTNMMzkuNDQgMTMuNDdMNDAuOTEgMTMuNDdMNDAuOTEgMTkuMTdRNDAuOTEgMjAuNTMgNDAuMDQgMjEuMzJRMzkuMTcgMjIuMTIgMzcuNzMgMjIuMTJMMzcuNzMgMjIuMTJRMzYuMjYgMjIuMTIgMzUuNDAgMjEuMzNRMzQuNTQgMjAuNTUgMzQuNTQgMTkuMTZaTTQ2Ljk3IDIyTDQ1LjQ4IDIyTDQ1LjQ4IDEzLjQ3TDQ4LjQ4IDEzLjQ3UTQ5Ljk2IDEzLjQ3IDUwLjc2IDE0LjEzUTUxLjU2IDE0Ljc5IDUxLjU2IDE2LjA1TDUxLjU2IDE2LjA1UTUxLjU2IDE2LjkwIDUxLjE1IDE3LjQ4UTUwLjc0IDE4LjA2IDUwLjAwIDE4LjM3TDUwLjAwIDE4LjM3TDUxLjkyIDIxLjkyTDUxLjkyIDIyTDUwLjMzIDIyTDQ4LjYyIDE4LjcxTDQ2Ljk3IDE4LjcxTDQ2Ljk3IDIyWk00Ni45NyAxNC42Nkw0Ni45NyAxNy41Mkw0OC40OSAxNy41MlE0OS4yNCAxNy41MiA0OS42NiAxNy4xNVE1MC4wOCAxNi43NyA1MC4wOCAxNi4xMUw1MC4wOCAxNi4xMVE1MC4wOCAxNS40MyA0OS42OSAxNS4wNVE0OS4zMCAxNC42OCA0OC41MyAxNC42Nkw0OC41MyAxNC42Nkw0Ni45NyAxNC42NlpNNTYuNzQgMjJMNTUuMjAgMjJMNTguNDIgMTMuNDdMNTkuNzUgMTMuNDdMNjIuOTggMjJMNjEuNDMgMjJMNjAuNzMgMjAuMDFMNTcuNDMgMjAuMDFMNTYuNzQgMjJaTTU5LjA4IDE1LjI4TDU3Ljg1IDE4LjgyTDYwLjMyIDE4LjgyTDU5LjA4IDE1LjI4WiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iI0ZGRkZGRiIgeD0iODguNTIiLz48L3N2Zz4=) \n'
                        

                        '**Python Pandas: técnicas avançadas** \n'
                        '[Credential ID bf57632f-1780-4952-95fc-1d1c103e88b9](https://cursos.alura.com.br/certificate/4d6ffa65-6e39-47e5-9caf-538ffad253d7)'

                        ,style={'white-space': 'pre'}),
        ], width=5)
    ], justify='center'),



    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2022 



                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),


        dbc.Col([
            
            dcc.Markdown(
                        '![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NS41MiIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDc1LjUyIDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iNzUuNTIiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDFFNDUiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI3NS41MiIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiMzODlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuMDAgMjJMMTMuNDYgMjJMMTYuNjggMTMuNDdMMTguMDEgMTMuNDdMMjEuMjQgMjJMMTkuNjkgMjJMMTguOTkgMjAuMDFMMTUuNjkgMjAuMDFMMTUuMDAgMjJaTTE3LjM0IDE1LjI4TDE2LjEwIDE4LjgyTDE4LjU4IDE4LjgyTDE3LjM0IDE1LjI4Wk0zMC41NSAyMkwyNS4xOSAyMkwyNS4xOSAxMy40N0wyNi42NyAxMy40N0wyNi42NyAyMC44MkwzMC41NSAyMC44MkwzMC41NSAyMlpNMzQuNTQgMTkuMTZMMzQuNTQgMTkuMTZMMzQuNTQgMTMuNDdMMzYuMDEgMTMuNDdMMzYuMDEgMTkuMThRMzYuMDEgMjAuMDMgMzYuNDUgMjAuNDhRMzYuODggMjAuOTMgMzcuNzMgMjAuOTNMMzcuNzMgMjAuOTNRMzkuNDQgMjAuOTMgMzkuNDQgMTkuMTNMMzkuNDQgMTkuMTNMMzkuNDQgMTMuNDdMNDAuOTEgMTMuNDdMNDAuOTEgMTkuMTdRNDAuOTEgMjAuNTMgNDAuMDQgMjEuMzJRMzkuMTcgMjIuMTIgMzcuNzMgMjIuMTJMMzcuNzMgMjIuMTJRMzYuMjYgMjIuMTIgMzUuNDAgMjEuMzNRMzQuNTQgMjAuNTUgMzQuNTQgMTkuMTZaTTQ2Ljk3IDIyTDQ1LjQ4IDIyTDQ1LjQ4IDEzLjQ3TDQ4LjQ4IDEzLjQ3UTQ5Ljk2IDEzLjQ3IDUwLjc2IDE0LjEzUTUxLjU2IDE0Ljc5IDUxLjU2IDE2LjA1TDUxLjU2IDE2LjA1UTUxLjU2IDE2LjkwIDUxLjE1IDE3LjQ4UTUwLjc0IDE4LjA2IDUwLjAwIDE4LjM3TDUwLjAwIDE4LjM3TDUxLjkyIDIxLjkyTDUxLjkyIDIyTDUwLjMzIDIyTDQ4LjYyIDE4LjcxTDQ2Ljk3IDE4LjcxTDQ2Ljk3IDIyWk00Ni45NyAxNC42Nkw0Ni45NyAxNy41Mkw0OC40OSAxNy41MlE0OS4yNCAxNy41MiA0OS42NiAxNy4xNVE1MC4wOCAxNi43NyA1MC4wOCAxNi4xMUw1MC4wOCAxNi4xMVE1MC4wOCAxNS40MyA0OS42OSAxNS4wNVE0OS4zMCAxNC42OCA0OC41MyAxNC42Nkw0OC41MyAxNC42Nkw0Ni45NyAxNC42NlpNNTYuNzQgMjJMNTUuMjAgMjJMNTguNDIgMTMuNDdMNTkuNzUgMTMuNDdMNjIuOTggMjJMNjEuNDMgMjJMNjAuNzMgMjAuMDFMNTcuNDMgMjAuMDFMNTYuNzQgMjJaTTU5LjA4IDE1LjI4TDU3Ljg1IDE4LjgyTDYwLjMyIDE4LjgyTDU5LjA4IDE1LjI4WiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iI0ZGRkZGRiIgeD0iODguNTIiLz48L3N2Zz4=) \n'
                        

                        '**Clustering: extraindo padrões de dados** \n'
                        '[Credential ID 3b5b2e9c-b00e-4c60-9b16-305cc0532463](https://cursos.alura.com.br/certificate/3b5b2e9c-b00e-4c60-9b16-305cc0532463)'

                        ,style={'white-space': 'pre'}),
        ], width=5)
    ], justify='center'),


    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2023



                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),




        dbc.Col([
            
            dcc.Markdown(
                        '![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NS41MiIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDc1LjUyIDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iNzUuNTIiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDFFNDUiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI3NS41MiIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiMzODlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuMDAgMjJMMTMuNDYgMjJMMTYuNjggMTMuNDdMMTguMDEgMTMuNDdMMjEuMjQgMjJMMTkuNjkgMjJMMTguOTkgMjAuMDFMMTUuNjkgMjAuMDFMMTUuMDAgMjJaTTE3LjM0IDE1LjI4TDE2LjEwIDE4LjgyTDE4LjU4IDE4LjgyTDE3LjM0IDE1LjI4Wk0zMC41NSAyMkwyNS4xOSAyMkwyNS4xOSAxMy40N0wyNi42NyAxMy40N0wyNi42NyAyMC44MkwzMC41NSAyMC44MkwzMC41NSAyMlpNMzQuNTQgMTkuMTZMMzQuNTQgMTkuMTZMMzQuNTQgMTMuNDdMMzYuMDEgMTMuNDdMMzYuMDEgMTkuMThRMzYuMDEgMjAuMDMgMzYuNDUgMjAuNDhRMzYuODggMjAuOTMgMzcuNzMgMjAuOTNMMzcuNzMgMjAuOTNRMzkuNDQgMjAuOTMgMzkuNDQgMTkuMTNMMzkuNDQgMTkuMTNMMzkuNDQgMTMuNDdMNDAuOTEgMTMuNDdMNDAuOTEgMTkuMTdRNDAuOTEgMjAuNTMgNDAuMDQgMjEuMzJRMzkuMTcgMjIuMTIgMzcuNzMgMjIuMTJMMzcuNzMgMjIuMTJRMzYuMjYgMjIuMTIgMzUuNDAgMjEuMzNRMzQuNTQgMjAuNTUgMzQuNTQgMTkuMTZaTTQ2Ljk3IDIyTDQ1LjQ4IDIyTDQ1LjQ4IDEzLjQ3TDQ4LjQ4IDEzLjQ3UTQ5Ljk2IDEzLjQ3IDUwLjc2IDE0LjEzUTUxLjU2IDE0Ljc5IDUxLjU2IDE2LjA1TDUxLjU2IDE2LjA1UTUxLjU2IDE2LjkwIDUxLjE1IDE3LjQ4UTUwLjc0IDE4LjA2IDUwLjAwIDE4LjM3TDUwLjAwIDE4LjM3TDUxLjkyIDIxLjkyTDUxLjkyIDIyTDUwLjMzIDIyTDQ4LjYyIDE4LjcxTDQ2Ljk3IDE4LjcxTDQ2Ljk3IDIyWk00Ni45NyAxNC42Nkw0Ni45NyAxNy41Mkw0OC40OSAxNy41MlE0OS4yNCAxNy41MiA0OS42NiAxNy4xNVE1MC4wOCAxNi43NyA1MC4wOCAxNi4xMUw1MC4wOCAxNi4xMVE1MC4wOCAxNS40MyA0OS42OSAxNS4wNVE0OS4zMCAxNC42OCA0OC41MyAxNC42Nkw0OC41MyAxNC42Nkw0Ni45NyAxNC42NlpNNTYuNzQgMjJMNTUuMjAgMjJMNTguNDIgMTMuNDdMNTkuNzUgMTMuNDdMNjIuOTggMjJMNjEuNDMgMjJMNjAuNzMgMjAuMDFMNTcuNDMgMjAuMDFMNTYuNzQgMjJaTTU5LjA4IDE1LjI4TDU3Ljg1IDE4LjgyTDYwLjMyIDE4LjgyTDU5LjA4IDE1LjI4WiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iI0ZGRkZGRiIgeD0iODguNTIiLz48L3N2Zz4=) \n'
                        

                        '**Redes Neurais: Deep Learning com PyTorch** \n'
                        '[Credential ID 8504fda3-63d9-4dde-9bee-8d32a338a1a8](https://cursos.alura.com.br/certificate/8504fda3-63d9-4dde-9bee-8d32a338a1a8)'

                        ,style={'white-space': 'pre'}),
        ], width=5),
    ], justify='center'),


    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2023



                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),




        dbc.Col([
            
            dcc.Markdown(
                        '![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NS41MiIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDc1LjUyIDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iNzUuNTIiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDFFNDUiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI3NS41MiIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiMzODlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuMDAgMjJMMTMuNDYgMjJMMTYuNjggMTMuNDdMMTguMDEgMTMuNDdMMjEuMjQgMjJMMTkuNjkgMjJMMTguOTkgMjAuMDFMMTUuNjkgMjAuMDFMMTUuMDAgMjJaTTE3LjM0IDE1LjI4TDE2LjEwIDE4LjgyTDE4LjU4IDE4LjgyTDE3LjM0IDE1LjI4Wk0zMC41NSAyMkwyNS4xOSAyMkwyNS4xOSAxMy40N0wyNi42NyAxMy40N0wyNi42NyAyMC44MkwzMC41NSAyMC44MkwzMC41NSAyMlpNMzQuNTQgMTkuMTZMMzQuNTQgMTkuMTZMMzQuNTQgMTMuNDdMMzYuMDEgMTMuNDdMMzYuMDEgMTkuMThRMzYuMDEgMjAuMDMgMzYuNDUgMjAuNDhRMzYuODggMjAuOTMgMzcuNzMgMjAuOTNMMzcuNzMgMjAuOTNRMzkuNDQgMjAuOTMgMzkuNDQgMTkuMTNMMzkuNDQgMTkuMTNMMzkuNDQgMTMuNDdMNDAuOTEgMTMuNDdMNDAuOTEgMTkuMTdRNDAuOTEgMjAuNTMgNDAuMDQgMjEuMzJRMzkuMTcgMjIuMTIgMzcuNzMgMjIuMTJMMzcuNzMgMjIuMTJRMzYuMjYgMjIuMTIgMzUuNDAgMjEuMzNRMzQuNTQgMjAuNTUgMzQuNTQgMTkuMTZaTTQ2Ljk3IDIyTDQ1LjQ4IDIyTDQ1LjQ4IDEzLjQ3TDQ4LjQ4IDEzLjQ3UTQ5Ljk2IDEzLjQ3IDUwLjc2IDE0LjEzUTUxLjU2IDE0Ljc5IDUxLjU2IDE2LjA1TDUxLjU2IDE2LjA1UTUxLjU2IDE2LjkwIDUxLjE1IDE3LjQ4UTUwLjc0IDE4LjA2IDUwLjAwIDE4LjM3TDUwLjAwIDE4LjM3TDUxLjkyIDIxLjkyTDUxLjkyIDIyTDUwLjMzIDIyTDQ4LjYyIDE4LjcxTDQ2Ljk3IDE4LjcxTDQ2Ljk3IDIyWk00Ni45NyAxNC42Nkw0Ni45NyAxNy41Mkw0OC40OSAxNy41MlE0OS4yNCAxNy41MiA0OS42NiAxNy4xNVE1MC4wOCAxNi43NyA1MC4wOCAxNi4xMUw1MC4wOCAxNi4xMVE1MC4wOCAxNS40MyA0OS42OSAxNS4wNVE0OS4zMCAxNC42OCA0OC41MyAxNC42Nkw0OC41MyAxNC42Nkw0Ni45NyAxNC42NlpNNTYuNzQgMjJMNTUuMjAgMjJMNTguNDIgMTMuNDdMNTkuNzUgMTMuNDdMNjIuOTggMjJMNjEuNDMgMjJMNjAuNzMgMjAuMDFMNTcuNDMgMjAuMDFMNTYuNzQgMjJaTTU5LjA4IDE1LjI4TDU3Ljg1IDE4LjgyTDYwLjMyIDE4LjgyTDU5LjA4IDE1LjI4WiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iI0ZGRkZGRiIgeD0iODguNTIiLz48L3N2Zz4=) \n'
                        

                        '**Treinando uma Rede Neural: Deep Learning com PyTorch** \n'
                        '[Credential ID 8ec52bf3-b146-4939-a075-fcc58887cd11](https://cursos.alura.com.br/certificate/8ec52bf3-b146-4939-a075-fcc58887cd11)'

                        ,style={'white-space': 'pre'}),
        ], width=5),
    ], justify='center'),
    

    ], title = 'Ciência de Dados' ),]),











#### Web e Mobile

dbc.Accordion([

  dbc.AccordionItem([

    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2022 



                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),

        dbc.Col([
            
            dcc.Markdown(
                        '![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NS41MiIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDc1LjUyIDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iNzUuNTIiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDFFNDUiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI3NS41MiIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiMzODlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuMDAgMjJMMTMuNDYgMjJMMTYuNjggMTMuNDdMMTguMDEgMTMuNDdMMjEuMjQgMjJMMTkuNjkgMjJMMTguOTkgMjAuMDFMMTUuNjkgMjAuMDFMMTUuMDAgMjJaTTE3LjM0IDE1LjI4TDE2LjEwIDE4LjgyTDE4LjU4IDE4LjgyTDE3LjM0IDE1LjI4Wk0zMC41NSAyMkwyNS4xOSAyMkwyNS4xOSAxMy40N0wyNi42NyAxMy40N0wyNi42NyAyMC44MkwzMC41NSAyMC44MkwzMC41NSAyMlpNMzQuNTQgMTkuMTZMMzQuNTQgMTkuMTZMMzQuNTQgMTMuNDdMMzYuMDEgMTMuNDdMMzYuMDEgMTkuMThRMzYuMDEgMjAuMDMgMzYuNDUgMjAuNDhRMzYuODggMjAuOTMgMzcuNzMgMjAuOTNMMzcuNzMgMjAuOTNRMzkuNDQgMjAuOTMgMzkuNDQgMTkuMTNMMzkuNDQgMTkuMTNMMzkuNDQgMTMuNDdMNDAuOTEgMTMuNDdMNDAuOTEgMTkuMTdRNDAuOTEgMjAuNTMgNDAuMDQgMjEuMzJRMzkuMTcgMjIuMTIgMzcuNzMgMjIuMTJMMzcuNzMgMjIuMTJRMzYuMjYgMjIuMTIgMzUuNDAgMjEuMzNRMzQuNTQgMjAuNTUgMzQuNTQgMTkuMTZaTTQ2Ljk3IDIyTDQ1LjQ4IDIyTDQ1LjQ4IDEzLjQ3TDQ4LjQ4IDEzLjQ3UTQ5Ljk2IDEzLjQ3IDUwLjc2IDE0LjEzUTUxLjU2IDE0Ljc5IDUxLjU2IDE2LjA1TDUxLjU2IDE2LjA1UTUxLjU2IDE2LjkwIDUxLjE1IDE3LjQ4UTUwLjc0IDE4LjA2IDUwLjAwIDE4LjM3TDUwLjAwIDE4LjM3TDUxLjkyIDIxLjkyTDUxLjkyIDIyTDUwLjMzIDIyTDQ4LjYyIDE4LjcxTDQ2Ljk3IDE4LjcxTDQ2Ljk3IDIyWk00Ni45NyAxNC42Nkw0Ni45NyAxNy41Mkw0OC40OSAxNy41MlE0OS4yNCAxNy41MiA0OS42NiAxNy4xNVE1MC4wOCAxNi43NyA1MC4wOCAxNi4xMUw1MC4wOCAxNi4xMVE1MC4wOCAxNS40MyA0OS42OSAxNS4wNVE0OS4zMCAxNC42OCA0OC41MyAxNC42Nkw0OC41MyAxNC42Nkw0Ni45NyAxNC42NlpNNTYuNzQgMjJMNTUuMjAgMjJMNTguNDIgMTMuNDdMNTkuNzUgMTMuNDdMNjIuOTggMjJMNjEuNDMgMjJMNjAuNzMgMjAuMDFMNTcuNDMgMjAuMDFMNTYuNzQgMjJaTTU5LjA4IDE1LjI4TDU3Ljg1IDE4LjgyTDYwLjMyIDE4LjgyTDU5LjA4IDE1LjI4WiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iI0ZGRkZGRiIgeD0iODguNTIiLz48L3N2Zz4=) \n'
                        

                        '**Dart: entendendo a Orientação a Objetos** \n'
                        '[Credential ID 33716798-f256-4bbe-969f-2eb585e678c1](https://cursos.alura.com.br/certificate/33716798-f256-4bbe-969f-2eb585e678c1)'

                        ,style={'white-space': 'pre'}),
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2023 



                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),

        dbc.Col([
            
            dcc.Markdown(
                        '![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NS41MiIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDc1LjUyIDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iNzUuNTIiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDFFNDUiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI3NS41MiIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiMzODlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuMDAgMjJMMTMuNDYgMjJMMTYuNjggMTMuNDdMMTguMDEgMTMuNDdMMjEuMjQgMjJMMTkuNjkgMjJMMTguOTkgMjAuMDFMMTUuNjkgMjAuMDFMMTUuMDAgMjJaTTE3LjM0IDE1LjI4TDE2LjEwIDE4LjgyTDE4LjU4IDE4LjgyTDE3LjM0IDE1LjI4Wk0zMC41NSAyMkwyNS4xOSAyMkwyNS4xOSAxMy40N0wyNi42NyAxMy40N0wyNi42NyAyMC44MkwzMC41NSAyMC44MkwzMC41NSAyMlpNMzQuNTQgMTkuMTZMMzQuNTQgMTkuMTZMMzQuNTQgMTMuNDdMMzYuMDEgMTMuNDdMMzYuMDEgMTkuMThRMzYuMDEgMjAuMDMgMzYuNDUgMjAuNDhRMzYuODggMjAuOTMgMzcuNzMgMjAuOTNMMzcuNzMgMjAuOTNRMzkuNDQgMjAuOTMgMzkuNDQgMTkuMTNMMzkuNDQgMTkuMTNMMzkuNDQgMTMuNDdMNDAuOTEgMTMuNDdMNDAuOTEgMTkuMTdRNDAuOTEgMjAuNTMgNDAuMDQgMjEuMzJRMzkuMTcgMjIuMTIgMzcuNzMgMjIuMTJMMzcuNzMgMjIuMTJRMzYuMjYgMjIuMTIgMzUuNDAgMjEuMzNRMzQuNTQgMjAuNTUgMzQuNTQgMTkuMTZaTTQ2Ljk3IDIyTDQ1LjQ4IDIyTDQ1LjQ4IDEzLjQ3TDQ4LjQ4IDEzLjQ3UTQ5Ljk2IDEzLjQ3IDUwLjc2IDE0LjEzUTUxLjU2IDE0Ljc5IDUxLjU2IDE2LjA1TDUxLjU2IDE2LjA1UTUxLjU2IDE2LjkwIDUxLjE1IDE3LjQ4UTUwLjc0IDE4LjA2IDUwLjAwIDE4LjM3TDUwLjAwIDE4LjM3TDUxLjkyIDIxLjkyTDUxLjkyIDIyTDUwLjMzIDIyTDQ4LjYyIDE4LjcxTDQ2Ljk3IDE4LjcxTDQ2Ljk3IDIyWk00Ni45NyAxNC42Nkw0Ni45NyAxNy41Mkw0OC40OSAxNy41MlE0OS4yNCAxNy41MiA0OS42NiAxNy4xNVE1MC4wOCAxNi43NyA1MC4wOCAxNi4xMUw1MC4wOCAxNi4xMVE1MC4wOCAxNS40MyA0OS42OSAxNS4wNVE0OS4zMCAxNC42OCA0OC41MyAxNC42Nkw0OC41MyAxNC42Nkw0Ni45NyAxNC42NlpNNTYuNzQgMjJMNTUuMjAgMjJMNTguNDIgMTMuNDdMNTkuNzUgMTMuNDdMNjIuOTggMjJMNjEuNDMgMjJMNjAuNzMgMjAuMDFMNTcuNDMgMjAuMDFMNTYuNzQgMjJaTTU5LjA4IDE1LjI4TDU3Ljg1IDE4LjgyTDYwLjMyIDE4LjgyTDU5LjA4IDE1LjI4WiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iI0ZGRkZGRiIgeD0iODguNTIiLz48L3N2Zz4=) \n'
                        

                        '**Dart: criando e manipulando variáveis e listas** \n'
                        '[Credential ID ad6cb6b7-9599-43be-95cf-00ef25cf7ed7](https://cursos.alura.com.br/certificate/ad6cb6b7-9599-43be-95cf-00ef25cf7ed7)'

                        ,style={'white-space': 'pre'}),
        ], width=5)
    ], justify='center'),



    ], title = 'Web & Mobile' ),]),





], className = 'col-sd-4')
