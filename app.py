import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1.0"}]
external_stylesheets = [
    meta_tags,
    font_awesome,
    dbc.themes.FLATLY
]

url_theme1 = dbc.themes.FLATLY
template_theme1 = "flatly"
url_theme2 = dbc.themes.DARKLY
template_theme2 = "darkly"

app = dash.Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)

server = app.server


theme_switch = ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2])

row = [

            dbc.Col([
                dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Nav([
                        dbc.NavLink(page["name"], href=page["path"])
                        for page in dash.page_registry.values()
                        if not page["path"].startswith("/app")
                    ]),
            ]),

            dbc.Col(
            [
            dbc.NavItem(theme_switch,
            className="text-primary d-flex align-items-right m-2", 
            ),
            ], align ='right')

]


header =dbc.Navbar(
    dbc.Container(
        [


            dbc.Row(row,justify = 'evenly'),

        ],
        fluid=True,

    ),
    dark=True,
    color='#87689c',
    style={'border-radius': 10}
)

app.layout = dbc.Container([header, dash.page_container], fluid=False)



if __name__ == '__main__':
	app.run_server(debug = True, port = '8090')