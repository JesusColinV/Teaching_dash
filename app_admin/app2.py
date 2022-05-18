from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from modulos.server import *
import dash_bootstrap_components as dbc
from modulos.components import *

builder = Builder()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


"""buttons = []
for i, lista in enumerate(configurationsTabs().buttons):
    if i != 2 or components[4][0]:  # recognizes when the clinical tab is disabled
        buttons.append(
            # the count starts at 0, one is added to match the ids in the callback
            myBuilder.make_btn(
                title_k=lista, class_k=f'myBtn{i+1} mt-3', id_k=f'MyBtn{i+1}')
        )"""


app = Dash(name='app_superadmi',
           server=server,
           url_base_pathname='/admin/',
           external_stylesheets=external_stylesheets,
           assets_url_path='..\assets'  # css
           )


app.layout = html.Div([

    # Component to detect the url
    dcc.Location(id='url', refresh=False),

    # Dashboard body
    dbc.Row([

        dbc.Col([  # The elements of the card are placed that filters the content
            dbc.Card(
                children=[
                    html.P(
                        'Fecha',
                        # style=myDrawer.TitleTextCardFilterDate,
                        className='texto'),
                    dcc.DatePickerRange(
                        id='mydatepiker',
                        # min_date_allowed=date(1995, 8, 5),
                        # max_date_allowed=date(2023, 9, 19),
                        # initial_visible_month=date(2017, 8, 5),
                        # end_date=date(2017, 8, 25)
                    ),

                    dbc.Button("Buscar", outline=True, className="myBtnSearch mt-3",
                               id="MyBtnSearch",
                               # style=myDrawer.stylebutton
                               ),
                    html.Div(
                        id='menusFilter',
                        className='MenusFilter mt-3',
                        # style=myDrawer.CardMenuFilter,
                        children=dbc.Spinner(
                            id="menusFilterSpinner",
                            # color=colors['spinner']
                        )

                    ),
                ],
                # style=myDrawer.CardMenuFilter,
                # color=colors['card2'],
                id='cardfilter',
                className='CardFilter mb-2',),

            dbc.Card(
                children=[
                    html.P('Exportar',
                           # style=myDrawer.TitleTextCardFilterDate,
                           className='mytitle texto', id="exportar"),
                    html.Div(
                        id='downloadFiles',
                        className='DownloadFiles',
                        # style=myDrawer.CardMenuFilter,
                        children=['boton1', 'boton2', 'boton3']
                    )
                ],
                # style=myDrawer.CardMenuFilter,
                # color=colors['card2'],
                id='cardDfiles',
                className='CardDFiles',),
        ]),

        # Contains the tabs to select
        html.Div([
                 dcc.Tabs(
                     id="tabs-styled",
                     value='tab-1',
                     # contruye las pestañas con las opciones activas
                     # children=
                     #  myDrawer.chooseTab(
                     #      components=components,
                     #     message=customName['messageHome']),
                 ),

                 ],
                 # End of the tab to choose
                 # style=myDrawer.styleMainTab,
                 id='tabstopics',
                 className="TabsTopics"),

    ],
        # End of Dashboard body
        id='body',
        className='Body',),

],
    # End of Dashboard
    id='mainContainer',
    className='MainContainer',
    # style=myDrawer.mainContainer
)
