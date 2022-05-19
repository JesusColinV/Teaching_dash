# SCRIPT DE AYUDA
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from modulos.server import *
import dash_bootstrap_components as dbc
from modulos.components import *
import pandas as pd

# Data
df = pd.read_excel(
    'C:/Users/alexi/OneDrive/Desktop/Portafolio_2/Teaching_dash/app_admin/Analisis de Portafolio.xlsx')

client = list(df['Cliente'])
client_list = []
for x in client:
    if x not in client_list:
        client_list.append(x)

sesion = list(df['Estatus de cesión'])
sesion_status = []
for status in sesion:
    if status not in sesion_status:
        sesion_status.append(status)
# print(sesion_status)

# df filtrado a los clientes con saldo insoluto mayor a 3 mdp

df_filtro_saldos = df[df['Saldo insoluto actual'] > 3000000]


builder = Builder()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def Tabs1():
    return html.Div([
        dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
            dcc.Tab(label='Gráfica 1', value='tab-1-example-graph'),
            dcc.Tab(label='Gráfica 2', value='tab-2-example-graph'),
        ]),
        html.Br(),
        html.Div(id='tabs-content-example-graph')
    ])


def drawFigure2():
    return html.Div(id='graph2')


def dropdown0():
    return html.Div([
        dcc.Dropdown(
            id="dropdown0",
            options=['Riesgo muy alto', 'Riesgo alto',
                     'Riesgo moderado', 'Sin riesgo'],
            value='Riesgo muy alto',
            clearable=False,
        )])


app = Dash(name='app_superadmi',
           server=server,
           url_base_pathname='/admin/',
           external_stylesheets=external_stylesheets,
           assets_url_path='..\assets'  # css
           )


app.layout = html.Div([
    # Component to detect the url
    dcc.Location(id='url', refresh=False),
    dbc.Row(builder.drawDescription('PORTAFOLIO DE CLIENTES'),
            id='main_title',
            className='main_title',),

    dbc.Row(Tabs1(),
            id='body',
            className='Body',),
    # html.Br(),
    # dbc.Row(
    #    html.Div(id='tabs-content-example-graph'),
    #    id='body2',
    #    className='graphs',),
    html.Br(),
    dbc.Row(builder.drawDescription('test')),
    html.Div(id='tabs-test')


],
    # End of Dashboard
    id='mainContainer',
    className='MainContainer',
)


# CALLBACK PRIMER TAB


@app.callback(Output('tabs-test', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    # print('opcion00')
    if tab == 'tab-1-example-graph':
        print('opcion1')
        return html.Div(builder.drawDescription('ESTAMOS EN TAB1'))
    elif tab == 'tab-2-example-graph':
        print('opcion2')
        return html.Div(builder.drawDescription('ESTAMOS EN TAB2'))


@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    # print('opcion0')
    if tab == 'tab-1-example-graph':
        print('opcion1')
        return html.Div(id='my_div0', children=[
            html.Div(children=[
                dbc.Row(builder.graphBarPx(
                    df=df_filtro_saldos, ejex='Cliente', ejey='Saldo insoluto actual', color='Perfil de riesgo', title='GRAFICA 1', color_discrete_map={
                        'Sin riesgo': 'blue',
                        'Riesgo moderado': 'yellow', 'Riesgo alto': 'orange', 'Riesgo muy alto': 'red'
                    }))])])
    elif tab == 'tab-2-example-graph':
        print('opcion2')
        return html.Div(id='my_div', children=[
            html.Div(children=[
                dbc.Row(builder.drawDescription('GRAFICA 2')),
                dbc.Row(dcc.Dropdown(
                    id="dropdown0",
                    options=['Riesgo muy alto', 'Riesgo alto',
                     'Riesgo moderado', 'Sin riesgo'],
                    value='Riesgo muy alto',
                    clearable=False,
                ))]),

            html.Div(children=[
                dbc.Row(
                    drawFigure2())])

        ])


@app.callback(
    Output("graph2", "children"),
    Input("dropdown0", "value"))
def update_bar_chart(Perfil):
    mask = df[df['Perfil de riesgo'] == Perfil]

    clientes = list(mask["Cliente"])
    y1 = list(mask["Saldo insoluto actual"])

    if Perfil == 'Riesgo muy alto':
        color0 = 'red'
    if Perfil == 'Riesgo alto':
        color0 = 'orange'
    if Perfil == 'Riesgo moderado':
        color0 = 'yellow'
    if Perfil == 'Sin riesgo':
        color0 = 'blue'

    clientes_saldos = go.Figure()
    clientes_saldos.add_trace(
        go.Bar(x=clientes, y=y1, name="Apalancamiento / ventas (autorizado)"))

    Perfil = Perfil.upper()
    tipo_perfil = Perfil

    clientes_saldos.update_layout(
        title=f"SALDOS INSOLUTOS DE CLIENTES CON PERFIL {tipo_perfil}",
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
    clientes_saldos.update_traces(marker_color=color0)
    return [html.Div([
        dcc.Graph(
            figure=clientes_saldos
        ),
    ])]
