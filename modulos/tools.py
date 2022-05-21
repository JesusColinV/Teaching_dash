import dash_bootstrap_components as dbc
from dash import dcc, html
from modulos.components import *


# Instanciando objeto
builder = Builder()


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


def drawFigure3():
    return html.Div(id='graph1')


def drawFigure5():
    return html.Div(id='graph3')


def drawFigure6(df):
    return html.Div(id='my_div5', className='miClase', children=[
        dbc.Card(children=[
            dbc.Row(builder.graphBarPx2(
                    df=df, ejex="Cliente", ejey=["Apalancamiento / ventas (autorizado)", "Apalancamiento / ventas (reales)"], title='TIPOS DE APALANCAMIENTO', barmode='group')
                    )
        ])]
    )


def drawFigure7():
    return html.Div(id='graph4')


def drawText8():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div(id='fact_mens_real', style={'textAlign': 'center'})
            ])
        ),
    ])


def graphRadar():

    fig = go.Figure(data=go.Scatterpolar(
        r=[1, 5, 2, 2, 3],
        theta=['processing cost', 'mechanical properties', 'chemical stability', 'thermal stability',
               'device integration'],
        fill='toself'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True
            ),
        ),
        showlegend=False
    )
    fig.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )
    return dbc.Card([
        dcc.Graph(
            figure=fig
        ),
    ])


def drawFigures1(client_list):
    # print()
    return html.Div(children=[
        html.Div(children=[dbc.Row(builder.drawParagraph(
                    f'SELECCIONA UNO DE LOS {len(client_list)} CLIENTES', 17, 'white')),
            dcc.Dropdown(
            id="dropdown1",
            options=client_list,
            value=client_list[1],
            clearable=False,
        ),
            drawFigure7()
        ], style={'width': '40%', 'display': 'inline-block'}),
        html.Div(children=[drawFigure3(),
                           drawText8()], style={
                 'width': '60%', 'display': 'inline-block'})
    ], style={'display': 'flex', 'align-items': 'center'})  # estilo que alinea horizontalmente los dos divs

# Metricas


def drawMetrics():
    return html.Div(id='metricas1')
