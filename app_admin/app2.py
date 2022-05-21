from modulos.tools import *
import math
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from modulos.server import *
import dash_bootstrap_components as dbc
from modulos.components import *
import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, '')

# Data
# df = pd.read_excel(
#    'C:/Users/alexi/OneDrive/Desktop/Portafolio_2/Teaching_dash/app_admin/Analisis de Portafolio.xlsx')

df = pd.read_excel(
    './app_admin/Analisis de Portafolio.xlsx')


#'./app_admin/Analisis de Portafolio.xlsx'

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
# TABS

builder = Builder()
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

external_stylesheets = [dbc.themes.SLATE]


"""
def Tabs1():
    return html.Div([
        dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
            dcc.Tab(label='Gráfica 1', value='tab-1-example-graph'),
            dcc.Tab(label='Gráfica 2', value='tab-2-example-graph'),
        ]),
        html.Br(),
        html.Div(id='tabs-content-example-graph')
    ])
"""


def Tabs2():
    return html.Div([
        dcc.Tabs(id="tabs-example-graph2", value='tab-1-example-graph', children=[
            dcc.Tab(label='FONDEADOR', value='tab-1-example-graph'),
            dcc.Tab(label='CESIÓN', value='tab-2-example-graph'),
            dcc.Tab(label='SECTOR', value='tab-3-example-graph'),
        ]),
        html.Div(id='tabs-content-example-graph2')
    ])


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
                dbc.Row(builder.drawDescriptionH1(
                    'PORTAFOLIO DE CLIENTES SMX'))
            ], width=12),
                align='center'),
            html.Br(),
            dbc.Row(dbc.Col([
                dbc.Row(builder.drawParagraph(
                    'SALDOS INSOLUTOS POR CLIENTE Y POR PERFIL DE RIESGO DEL CLIENTE', 17, 'white'))
            ], width=12),
                align='center'),
            dbc.Row(Tabs1(),
                    id='tab1',
                    className='Body',),
            html.Br(),
            dbc.Row(dbc.Col([
                dbc.Row(builder.drawParagraph(
                    'SALDOS INSOLUTOS POR FONDEADOR, POR ESTATUS DE CESIÓN Y POR SECTOR', 17, 'white'))
            ], width=12),
                align='center'),
            html.Br(),
            dbc.Row(Tabs2(),
                    id='tab2',
                    className='Body',),
            html.Br(),
            dbc.Row(dbc.Col([
                dbc.Row(builder.drawParagraph(
                    'SALDOS INSOLUTOS POR CLIENTE Y POR PERFIL DE RIESGO DEL CLIENTE', 17, 'white'))
            ], width=12),
                align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure6(df_filtro_saldos)
                ], width=12),
            ], align='center'),
            html.Br(),
            dbc.Row(dbc.Col([
                dbc.Row(builder.drawParagraph(
                    'APALANCAMIENTOS POR CLIENTE Y METRICAS PARTICULARES', 17, 'white'))
            ], width=12),
                align='center'),
            dbc.Row(
                drawFigures1(client_list)
            ),
            html.Br(),
            html.Div(drawMetrics())


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
                dbc.Row(dbc.Card(builder.graphBarPx(
                    df=df_filtro_saldos, ejex='Cliente', ejey='Saldo insoluto actual', color='Perfil de riesgo', title='GRAFICA 1', color_discrete_map={
                        'Sin riesgo': 'blue',
                        'Riesgo moderado': 'yellow', 'Riesgo alto': 'orange', 'Riesgo muy alto': 'red'
                    })))])], style={"width": "100%", "display": "block", "flex-direction": "row", "justify-content": "center"})
    elif tab == 'tab-2-example-graph':
        # print('opcion2')
        return html.Div(id='my_div', children=[
            html.Div(children=[
                dbc.Row(builder.drawParagraph(
                    'SELECCIONA EL CLIENTE POR TIPO DE PERFIL', 10, 'white')),
                dbc.Row(dcc.Dropdown(
                    id="dropdown0",
                    options=['Riesgo muy alto', 'Riesgo alto',
                             'Riesgo moderado', 'Sin riesgo'],
                    value='Riesgo muy alto',
                    clearable=False,
                ))]),

            dbc.Card(children=[
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
    #print('y1 y1')
    # print(y1)

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

    sum_saldos = locale.currency(
        sum(y1), grouping=True)

    clientes_saldos.update_layout(
        title=f"SALDOS INSOLUTOS DE CLIENTES CON PERFIL {tipo_perfil}<br><sup>SUMA DE SALDOS INSOLUTOS IGUAL A {sum_saldos}</sup>",
        xaxis_title="CLIENTES",
        legend_title="TIPO DE APALANCAMIENTO",
        font=dict(
            #family="Courier New, monospace",
            size=14,
            color="#fffffc"))
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
                dbc.Row(dbc.Card(builder.graphBarPx(
                    df=df, ejex="Fondeador", ejey="Saldo insoluto actual", title='SALDO INSOLUTO POR FONDEADOR', color='Perfil de riesgo', color_discrete_map={
                                'Sin riesgo': 'blue',
                                'Riesgo moderado': 'yellow', 'Riesgo alto': 'orange', 'Riesgo muy alto': 'red'
                    })))])], style={"width": "100%", "display": "block", "flex-direction": "row", "justify-content": "center"})
    elif tab == 'tab-2-example-graph':
        return html.Div(id='my_div3', children=[
            html.Div(children=[
                dbc.Row(dbc.Card(builder.drawParagraph(
                        'ESTATUS DE CESIÓN', 10, 'black')
                )),
                dbc.Row(dcc.Dropdown(
                    id="dropdown2",
                    options=sesion_status,
                    value=sesion_status[0],
                    clearable=False,
                )),
                dbc.Row(dbc.Card(drawFigure5()
                                 )),
            ])]
        )
    elif tab == 'tab-3-example-graph':
        return html.Div(id='my_div3', children=[
            html.Div(children=[
                dbc.Row(dbc.Card(builder.graphBarPx(df=df, ejex="Sector", ejey="Saldo insoluto actual", title='SALDO INSOLUTO POR SECTOR', color='Perfil de riesgo', color_discrete_map={
                    'Sin riesgo': 'blue',
                    'Riesgo moderado': 'yellow', 'Riesgo alto': 'orange', 'Riesgo muy alto': 'red'
                }
                )
                ))
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

    sum_saldos = locale.currency(
        sum(y1), grouping=True)

    clientes_saldos.update_layout(
        title=f"SALDOS INSOLUTOS POR TIPO DE ESTATUS DE CESIÓN<br><sup>SUMA DE SALDOS INSOLUTOS IGUAL A {sum_saldos}</sup>",
        xaxis_title="CLIENTES",
        legend_title="ESTATUS DE CESIÓN",
        font=dict(
            #family="Courier New, monospace",
            size=14,
            color="#fffffc"))
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


@app.callback(
    Output("fact_mens_real", "children"),
    Input("dropdown1", "value"))
def update_bar_chart(cliente):
    df2 = df[['Cliente', 'Facturación mensual real']]
    df3 = df2[df2['Cliente'] == cliente]
    df3 = df3['Facturación mensual real'].tolist()
    val = 'N/A'

    try:
        if df3[0] >= 1:
            val = df3[0]
            val = locale.currency(
                val, grouping=True)
    except:
        val = '$$'

    return html.H5(f"NETO DE LA FACTUACIÓN MENSUAL REAL DEL CLIENTE IGUAL A: {val}")


@app.callback(
    Output("graph1", "children"),
    Input("dropdown1", "value"))
def update_bar_chart(cliente):
    mask = df[df['Cliente'] == cliente]

    clientes = list(mask["Cliente"])
    y1 = list(mask["Apalancamiento / ventas (autorizado)"])
    y2 = list(mask['Apalancamiento / ventas (reales)'])

    clientes_saldos = go.Figure()
    clientes_saldos.add_trace(
        go.Bar(x=clientes, y=y1, name="Apalancamiento / ventas (autorizado)"))
    clientes_saldos.add_trace(
        go.Bar(x=clientes, y=y2, name="Apalancamiento / ventas (reales)"))

    clientes_saldos.update_layout(
        title="APALANCAMIENTO POR CLIENTE",
        xaxis_title="CLIENTES",
        legend_title="TIPO DE APALANCAMIENTO",
        font=dict(
            #family="Courier New, monospace",
            size=16,
            color="#fffffc"))
    clientes_saldos.update_layout(barmode='group')
    clientes_saldos.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )
    return dbc.Card([
        dcc.Graph(
            figure=clientes_saldos
        ),
    ])


@app.callback(
    Output("metricas1", "children"),
    Input("dropdown1", "value"))
def update_bar_chart(cliente):

    df2 = df[df['Cliente'] == cliente]
    df3 = df2['Facturación mensual real'].tolist()
    val = '$$'

    garantia = df2['Aforo real de garantía'].tolist()
    garantia = 'SI' if garantia[0] > 0 else 'NO'

    producto = df2['Producto'].tolist()
    producto = producto[0].upper()

    perfil = df2['Perfil de riesgo'].tolist()
    perfil = perfil[0].upper()

    pagadoresA = df2['Pagadores autorizados'].tolist()
    #print(f'el tipo de dato es igual a{type(pagadoresA)}')
    pagadoresA = pagadoresA[0].upper()
    # print(
    #    f'el tipo de dato es igual a{type(pagadoresA)}')

    pagadoresA = 'SIN PAGADORES AUTORIZADOS' if type(
        pagadoresA) == type(1.22) else pagadoresA

    retraso1 = df2['% de Retraso / saldo actual en (Buró de credito)'].tolist()
    retraso1 = round(retraso1[0], 2)
    # print(retraso1)
    retraso1 = 'N/A' if math.isnan(retraso1) else retraso1

    cesion = df2['Estatus de cesión'].tolist()
    cesion = cesion[0].upper()

    fondeador = df2['Fondeador'].tolist()
    fondeador = fondeador[0].upper()

    est_fact = df2['Estatus Facturación'].tolist()
    #print(f'est_fact -> {est_fact[0]}')
    est_fact = est_fact[0]

    try:
        est_fact = 'N/A' if math.isnan(est_fact) else est_fact
    except:
        pass

    est_fact = est_fact.upper()

    try:
        if df2[0] >= 1:
            val = df3[0]
            val = locale.currency(
                val, grouping=True)
    except:
        val = '$$'

    cliente = cliente.upper()

    # COLORES DE METRICAS

    # a = 1 if b==2 else (2 if b>3 else 3)

    Color1 = 'red' if garantia == 'NO' else 'green'

    #print(f'perfil {perfil}')
    if perfil == 'RIESGO MUY ALTO':
        Color2 = 'red'
    if perfil == 'RIESGO ALTO':
        Color2 = 'orange'
    if perfil == 'RIESGO MODERADO':
        Color2 = 'yellow'
    if perfil == 'SIN RIESGO':
        Color2 = 'green'

    Color3 = 'red' if retraso1 > 1 else 'green'
    Color4 = 'red' if cesion == 'POR CONFIRMAR' else 'green'
    Color5 = 'black'

    if est_fact == 'DETENIDA':
        Color5 = 'red'
    if est_fact == 'REDUCIDA' or est_fact == 'N/A':
        Color5 = 'orange'
    if est_fact == 'RETRASADA':
        Color5 = 'yellow'
    if est_fact == 'NORMAL':
        Color5 = 'green'
    # if est_fact == 'N/A':
    #    Color5 = 'green'

    #print(f'pagadoresA -> {len(pagadoresA)}')
    if len(pagadoresA) > 19:
        fontSizePayers = 22
    else:
        fontSizePayers = 30

    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.P(f"METRICAS PARTICULARES DEL CLIENTE '{cliente}'",
                       style={
                           'textAlign': 'center',
                           'color': 'white',
                           'fontSize': 30}
                       ),
                dbc.Row([
                    dbc.Col([
                            html.Div([
                                html.Div(id='box1', className='myMetric', children=[
                                    html.H6(children='GARANTÍA',
                                            style={
                                                'textAlign': 'center',
                                                'color': 'black'}),
                                    html.P(garantia,
                                           style={
                                               'textAlign': 'center',
                                               'color': Color1,
                                               'fontSize': 30}
                                           ),
                                ], style={'textAlign': 'center'})
                            ])
                            ], width=3),
                    dbc.Col([
                        html.Div([
                            html.Div(id='box2', className='myMetric', children=[
                                html.H6(children='PRODUCTO',
                                        style={
                                            'textAlign': 'center',
                                            'color': 'black'}),
                                html.P(producto,
                                       style={
                                           'textAlign': 'center',
                                           'color': 'black',
                                           'fontSize': 30}
                                       ),
                            ], style={'textAlign': 'center'})
                        ])
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.Div(id='box3', className='myMetric', children=[
                                html.H6(children='PERFIL DE RIESGO',
                                        style={
                                            'textAlign': 'center',
                                            'color': 'black'}),
                                html.P(perfil,
                                       style={
                                           'textAlign': 'center',
                                           'color': Color2,
                                           'fontSize': 30}
                                       ),
                            ], style={'textAlign': 'center'})
                        ])
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.Div(id='box4', className='myMetric', children=[
                                html.H6(children='PAGADORES AUTORIZADOS',
                                        style={
                                            'textAlign': 'center',
                                            'color': 'black'}),
                                html.P(pagadoresA,
                                       style={
                                           'textAlign': 'center',
                                           'color': 'black',
                                           'fontSize': fontSizePayers}
                                       ),
                            ], style={'textAlign': 'center'})
                        ])
                    ], width=3)

                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                            html.Div([
                                html.Div(id='box5', className='myMetric', children=[
                                    html.H6(children=' % DE RETRASO / SALDO ACTUAL EN BURÓ DE CRÉDITO ',
                                            style={
                                                'textAlign': 'center',
                                                'color': 'black',
                                                'fontSize': 13}),
                                    html.P(retraso1,
                                           style={
                                               'textAlign': 'center',
                                               'color': Color3,
                                               'fontSize': 27}
                                           ),
                                ], style={'textAlign': 'center'})
                            ])
                            ], width=3),
                    dbc.Col([
                        html.Div([
                            html.Div(id='box6', className='myMetric', children=[
                                html.H6(children='ESTATUS DE CESIÓN',
                                        style={
                                            'textAlign': 'center',
                                            'color': 'black'}),
                                html.P(cesion,
                                       style={
                                           'textAlign': 'center',
                                           'color': Color4,
                                           'fontSize': 30}
                                       ),
                            ], style={'textAlign': 'center'})
                        ])
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.Div(id='box7', className='myMetric', children=[
                                html.H6(children='FONDEADOR',
                                        style={
                                            'textAlign': 'center',
                                            'color': 'black'}),
                                html.P(fondeador,
                                       style={
                                           'textAlign': 'center',
                                           'color': 'black',
                                           'fontSize': 30}
                                       ),
                            ], style={'textAlign': 'center'})
                        ])
                    ], width=3),
                    dbc.Col([
                        html.Div([
                            html.Div(id='box8', className='myMetric', children=[
                                html.H6(children='ESTATUS FACTURACIÓN',
                                        style={
                                            'textAlign': 'center',
                                            'color': 'black'}),
                                html.P(est_fact,
                                       style={
                                           'textAlign': 'center',
                                           'color': Color5,
                                           'fontSize': 30}
                                       ),
                            ], style={'textAlign': 'center'}
                            )
                        ])
                    ], width=3)

                ], align='center')
            ])
        )
    ])
