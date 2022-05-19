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

# df filtrado a los clientes con saldo insoluto mayor a 3 mdp

df_filtro_saldos = df[df['Saldo insoluto actual'] > 3000000]

# COLORES

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


###


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


def Tabs2():
    return html.Div([
        dcc.Tabs(id="tabs-example-graph2", value='tab-1-example-graph', children=[
            dcc.Tab(label='FONDEADOR', value='tab-1-example-graph'),
            dcc.Tab(label='CESIÓN', value='tab-2-example-graph'),
            dcc.Tab(label='SECTOR', value='tab-3-example-graph'),
        ]),
        html.Div(id='tabs-content-example-graph2')
    ])


def drawFigure2():
    return html.Div(id='graph2')


def drawFigure5():
    return html.Div(id='graph3')


app = Dash(name='app_superadmi',
           server=server,
           url_base_pathname='/admin/',
           external_stylesheets=external_stylesheets,
           assets_url_path='..\assets'  # css
           )


app.layout = html.Div([
    # Component to detect the url
    dcc.Location(id='url', refresh=False),
    dbc.Card(
        dbc.CardBody(children=[
            dbc.Row(dbc.Col([
                dbc.Row(builder.drawDescriptionH4('PORTAFOLIO DE CLIENTES'))
            ], width=12),
                align='center'),
            html.Br(),
            dbc.Row(dbc.Col([
                dbc.Row(builder.drawParagraph(
                    'SALDOS INSOLUTOS POR CLIENTE Y POR PERFIL DE RIESGO DEL CLIENTE', 17, 'black'))
            ], width=12),
                align='center'),
            dbc.Row(Tabs1(),
                    id='tab1',
                    className='Body',),
            html.Br(),
            dbc.Row(dbc.Col([
                dbc.Row(builder.drawParagraph(
                    'SALDOS INSOLUTOS POR FONDEADOR, POR ESTATUS DE CESIÓN Y POR SECTOR', 17, 'black'))
            ], width=12),
                align='center'),
            html.Br(),
            dbc.Row(Tabs2(),
                    id='tab2',
                    className='Body',),
            html.Br(),
            # dbc.Row([
            #    dbc.Col([
            #        drawFigure2()
            #    ], width=12),
            # ], align='center'),


        ]), color='dark')
],
    # End of Dashboard
    id='mainContainer',
    className='MainContainer',
)


# CALLBACK PRIMER TAB


@app.callback(Output('tabs-test', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-1-example-graph':
        # print('opcion1')
        return html.Div(builder.drawDescriptionH5('ESTAMOS EN TAB1'))
    elif tab == 'tab-2-example-graph':
        # print('opcion2')
        return html.Div(builder.drawDescriptionH5('ESTAMOS EN TAB2'))


@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    # print('opcion0')
    if tab == 'tab-1-example-graph':
        # print('opcion1')
        return html.Div(id='my_div0', children=[
            html.Div(children=[
                dbc.Row(builder.graphBarPx(
                    df=df_filtro_saldos, ejex='Cliente', ejey='Saldo insoluto actual', color='Perfil de riesgo', title='GRAFICA 1', color_discrete_map={
                        'Sin riesgo': 'blue',
                        'Riesgo moderado': 'yellow', 'Riesgo alto': 'orange', 'Riesgo muy alto': 'red'
                    }))])], style={"width": "100%", "display": "block", "flex-direction": "row", "justify-content": "center"})
    elif tab == 'tab-2-example-graph':
        # print('opcion2')
        return html.Div(id='my_div', children=[
            html.Div(children=[
                dbc.Row(builder.drawParagraph(
                    'SELECCIONA EL CLIENTE POR TIPO DE PERFIL', 10, 'black')),
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

        ], style={"width": "100%", "display": "block", "flex-direction": "row", "justify-content": "center"})


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
            color="#0a0a0a"))
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

# CALLBACK TAB2


@app.callback(Output('tabs-content-example-graph2', 'children'),
              Input('tabs-example-graph2', 'value'))
def render_content(tab):
    if tab == 'tab-1-example-graph':
        return html.Div(id='my_div2', children=[
            html.Div(children=[
                dbc.Row(builder.graphBarPx(
                    df=df, ejex="Fondeador", ejey="Saldo insoluto actual", title='SALDO INSOLUTO POR FONDEADOR', color='Perfil de riesgo', color_discrete_map={
                                'Sin riesgo': 'blue',
                                'Riesgo moderado': 'yellow', 'Riesgo alto': 'orange', 'Riesgo muy alto': 'red'
                    }))])], style={"width": "100%", "display": "block", "flex-direction": "row", "justify-content": "center"})
    elif tab == 'tab-2-example-graph':
        return html.Div(id='my_div3', children=[
            html.Div(children=[
                dbc.Row(builder.drawParagraph(
                        'ESTATUS DE CESIÓN', 10, 'black')
                        ),
                dbc.Row(dcc.Dropdown(
                    id="dropdown2",
                    options=sesion_status,
                    value=sesion_status[0],
                    clearable=False,
                )),
                dbc.Row([drawFigure5()
                         ]),
            ])]
        )
    elif tab == 'tab-3-example-graph':
        return html.Div(id='my_div3', children=[
            html.Div(children=[
                dbc.Row(builder.graphBarPx(
                    df, x="Sector", y="Saldo insoluto actual", title='SALDO INSOLUTO POR SECTOR', color='Perfil de riesgo', color_discrete_map={
                        'Sin riesgo': 'blue',
                        'Riesgo moderado': 'yellow', 'Riesgo alto': 'orange', 'Riesgo muy alto': 'red'
                    }
                )
                )
            ])]
        )


@app.callback(
    Output("graph3", "children"),
    Input("dropdown2", "value"))
def update_bar_chart(status):
    mask = df[df['Estatus de cesión'] == status]

    clientes = list(mask["Cliente"])
    y1 = list(mask["Saldo insoluto actual"])

    clientes_saldos = go.Figure()
    clientes_saldos.add_trace(
        go.Bar(x=clientes, y=y1, name="Estatus de cesión"))

    clientes_saldos.update_layout(
        title="SALDOS INSOLUTOS POR TIPO DE ESTATUS DE CESIÓN",
        xaxis_title="CLIENTES",
        legend_title="ESTATUS DE CESIÓN",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#0a0a0a"))
    clientes_saldos.update_layout(barmode='stack')
    clientes_saldos.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )
    return html.Div([
        dcc.Graph(
            figure=clientes_saldos
        ),
    ])
