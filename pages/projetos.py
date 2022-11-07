import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar
import numpy as np
import gc



dash.register_page(__name__, title='Projetos', order=1)

header = html.Div([
    html.Br(),
    html.Br(),
    # html.Br(),
    # html.Br(),

    # html.H3('Projetos de aplicações web para visualização de dados'),

    dcc.Markdown(
        '''

        ### Olá, seja bem vindx à minha página de projetos! 👋


        Nessa página apresento alguns projetos de Análise e Visualização de Dados. 
        Tenho me dedicado a transformar os meus projetos em Aplicações Web para facilitar o compartilhamento e 
        apresentação desses projetos. Nesta página apresento alguns deles.

        ----

        '''
        ),
    html.Br(),

dbc.Accordion([

  dbc.AccordionItem([

        dcc.Markdown(
    
            '''
    
            A PEDEA é uma plataforma que apresenta dados ambientais diversos a partir de um servidor geográfico. 
            A plataforma foi desenvolvida no âmbito do Programa Cientista Chefe em Meio Ambiente em parceria com a 
            Secretaria do Meio Ambiente do Estado do Ceará. O objetivo do projeto Sig Ambiental é criar um repositório 
            de dados ambientais e disponibilizar estes dados em benefício da sociedade civil e órgãos de gestão do Estado. 
            Para isso, foi adquirido diversos dados georreferenciados que foram processados e disponibilizados na plataforma.
    
            A plataforma foi desenvolvida em React sendo alimentada a partir do Geoserver e banco de dados PostGIS. 
            Minhas atribuições nesse projeto estão relacionadas à aquisição e análise dos dados e auxílio na alimentação
            do banco de dados, bem como a realização de testes automatizados e divulgação da plataforma.
    
            '''
            ),
    
    
            html.P('Clique na imagem para ser direcionado à plataforma'),
            html.A([
            html.Img(
            src='assets/PEDEA.png',
            style={
                'height' : '80%',
                'width' : '80%',
                'align-items':'center',
            })
            ], href='https://pedea.sema.ce.gov.br/portal/', style={'align-items': 'center'}),
    
            html.Br(),
            html.Br(),
    
    ], title = 'Plataforma Estadual de Dados Ambientais (PEDEA)' ),

    dbc.AccordionItem([
        dcc.Markdown(

                '''

                
                O projeto Find My Address surgiu de uma necessidade da minha equipe de trabalho para encontrar as coordenadas
                de um endereço. Podemos encontrar as coordenadas de um dado endereço utilizando a biblioteca 
                [Geopy](https://geopy.readthedocs.io/en/stable/). Trata-se de um trabalho simples de se realizar em sua maquina local,
                como segue no exemplo abaixo:

                ```python


                from geopy.geocoders import Nominatim

                geolocator = Nominatim(user_agent="MyApp")
                location = geolocator.geocode('Cidade Universitaria, São Paulo')

                print(location)

                Out: Location(Cidade Universitária Armando de Salles Oliveira, Avenida Arruda Botelho, Alto de Pinheiros, 
                São Paulo, Região Imediata de São Paulo, Região Metropolitana de São Paulo, Região Geográfica Intermediária de São Paulo, 
                São Paulo, Região Sudeste, 05466-000, Brasil, (-23.56096405, -46.72770807289966, 0.0))


                Para uma melhor visualização do processo e para a utilização do algoritmo por colegas que não trabalham com python, desenvolvi 
                a aplicação abaixo para realizar esta consulta:


                '''
                ),


                html.P('Clique na imagem para ser direcionado à aplicação'),
                html.A([
                html.Img(
                src='assets/find.png',
                style={
                    'height' : '80%',
                    'width' : '80%',
                })
                ], href='https://find-my-address.onrender.com/', style={'align-items': 'center'}),

                html.Br(),
                html.Br(),

        ],title = 'Find My Address 🌎'),

        dbc.AccordionItem([
            dcc.Markdown(
                '''


                O Banco Nacional de Dados Oceanográficos(BNDO) é uma coletânea de dados oceanográficos admnistrado pela Marinha do Brasil. 
                Os dados do BNDO integram o [Atlas Digital Costeiro e Marinho](https://www.sema.ce.gov.br/89965-2/planejamento-costeiro-e-marinho-do-ceara/atlas-digital-costeiro-e-marinho-do-ceara/)
                que foi publicado no ano de 2021 no âmbito do Programa Cientista Chefe em Meio Ambiente do qual faço parte. 
                Para auxiliar na visualização dos dados, desenvolvi um dashboard para selecionar os dados de interesse e favorecer o download desses dados
                por meio de uma tabela.

                O dashboard foi desenvolvido em python utilizando as bibliotecas [Dash e Plotly](https://dash.plotly.com/) e publicado utilizando o Google Cloud Plataform:

                '''

                ),



            html.P('Clique na imagem para ser direcionado ao dashboard'),
            html.A([
            html.Img(
            src='assets/bndo.png',
            style={
                'height' : '80%',
                'width' : '80%',
            })
            ], href='http://dash-bndo.uc.r.appspot.com/', style={'align-items': 'center'}),

        ],title = 'Dashboard BNDO 🌊'),


        dbc.AccordionItem([
            dcc.Markdown(
                '''

                --------


                ### Web Search 🔎


                Projeto de Web Scraping para acessar páginas web fazer a busca de umas string dentro de links dentro desta página.
                O projeto surgiu da necessidade de conferir os links de download de metadados dentro da Plataforma Estadual de Dados 
                Ambientais do Estado do Ceará. O algoritmo realiza uma busca na pagina fornecida e acessa todos os links da classe html 
                fornecida pelo usuário. Para realizar essa tarefa foi utilizado a biblioteca [Selenium](https://selenium-python.readthedocs.io/).

                No exemplo abaixo, é realizado uma busca pela string 'HTTP Status 404', nos links da classe 'MetaLink', no site da plataforma.
                Os links em que a string foi encontrada são apresentados em uma tabela, como mostrado no exemplo abaixo:




                '''

                ),



            html.Img(
            src='assets/web.png',
            style={
                'height' : '80%',
                'width' : '80%',
                'textAlign':'center'
            }),


            html.Br(),

            html.Br(),

            html.Br(),


            dcc.Markdown(
                '''

                O algoritmo para fazer a busca na maquina local é relativamente simples: 


                ```python

                from selenium import webdriver

                string_busca = 'HTTP Status 404'
                driver = webdriver.Chrome()
                #Acessando o site que será realizado a busca
                driver.get("http://pedea.sema.ce.gov.br/portal/")
                #Encontrando os elementos por classe
                elements = driver.find_elements(By.CLASS_NAME, 'MetaLink')
                #Criando lista de endereços com todos os elementos
                metalinks = [element.get_attribute('href') for element in elements]
                #Loop para encontrar as páginas que contém a string de busca
                links = []
                for href in metalinks:
                    driver.get(href)
                    if string_busca in driver.page_source:
                        links.append(href)

                '''

                ),
        ], title = 'Web Search 🔎'),
])
])

def layout():
    return html.Div([header

        ])