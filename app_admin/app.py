from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from modulos.server import *
import dash_bootstrap_components as dbc
from modulos.components import *
import pandas as pd

df = pd.read_excel('app_admin\Analisis de Portafolio.xlsx')

# VARIABLES ESTATICAS

client = list(df['Cliente'])
CLIENT_LIST = []
for x in client:
    if x not in CLIENT_LIST:
        CLIENT_LIST.append(x)

sesion = list(df['Estatus de cesión'])
SESION_STATUS = []
for status in sesion:
    if status not in SESION_STATUS:
        SESION_STATUS.append(status)


builder = Builder()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def dropdown0():
    return html.Div([
        dcc.Dropdown(
            id="dropdown0",
            options=['White', 'Yellow', 'Orange', 'Red'],
            value='White',
            clearable=False,
        )])


dbc.Row([
        html.Div([
            dcc.Dropdown(
                id="dropdown1",
                options=CLIENT_LIST,
                value=CLIENT_LIST[0],
                clearable=False,
            )])]),


app = Dash(name='app_superadmi',
           server=server,
           url_base_pathname='/admin/',
           external_stylesheets=external_stylesheets,
           assets_url_path='..\assets'  # css
           )


app.layout = html.Div([
    # Component to detect the url
    dcc.Location(id='url', refresh=False),

    dbc.Row([
        dbc.Card(
            children=builder.graphBarPx(
                df=df, ejex='Sector', ejey='Saldo insoluto actual', title='Titulo de la grafica'),
            id='graph1',
            className='CardFilter mb-2',),

    ],
        # End of Dashboard body
        id='body',
        className='Body',),
    dbc.Row([
        html.Div([
            dcc.Dropdown(
                id="dropdown0",
                options=['White', 'Yellow', 'Orange', 'Red'],
                value='White',
                clearable=False,
            )])

    ]),

    dbc.Row([

        html.Div(id='graph2')



    ],
        # End of Dashboard body
        id='body2',
        className='Body',),

],
    # End of Dashboard
    id='mainContainer',
    className='MainContainer',
)


@app.callback(
    Output("graph2", "children"),
    Input("dropdown0", "value"))
def update_bar_chart(clas):
    # print(clas)
    # print(df.columns)
    # print(df['Clas'].tolist())
    mask = df[df['Clas'] == clas]

    clientes = list(mask["Cliente"])
    y1 = list(mask["Saldo insoluto actual"])

    clientes_saldos = go.Figure()
    clientes_saldos.add_trace(
        go.Bar(x=clientes, y=y1, name="% de Apalancamiento/ventas anuales autorizado"))

    clientes_saldos.update_layout(
        title="SALDOS INSOLUTOS POR TIPO DE CLIENTE",
        xaxis_title="CLIENTES",
        legend_title="TIPO DE APALANCAMIENTO",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#fcfcfc"))
    clientes_saldos.update_layout(barmode='stack')
    clientes_saldos.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )
    return [html.Div([
        dcc.Graph(
            figure=clientes_saldos
        ),
    ])]
