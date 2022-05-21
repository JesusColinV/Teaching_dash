from dash import dcc
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
import dash_html_components as html
import dash_bootstrap_components as dbc


class Builder:
    def __init__(self):
        pass

    def rangePiker(self, *args, **kwargs):
        """
        El elemento input de rango de fechas es retornado
        """
        return dcc.DatePickerRange(
            id=kwargs['id'],
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2023, 9, 19),
            initial_visible_month=date(2017, 8, 5),
            end_date=date(2017, 8, 25)
        )

    # GRAFICAS
    def graphBarPx(self, *args, **kwargs):
        self.df = kwargs['df']
        self.ejex = kwargs['ejex']
        self.ejey = kwargs['ejey']
        self.title = kwargs['title']
        self.color = kwargs['color']
        self.color_discrete_map = kwargs['color_discrete_map']
        """
        Elemento grafica de barras (px bar) retornado
        """

        px_bar = px.bar(self.df,
                        x=self.ejex,
                        y=self.ejey,
                        title=self.title,
                        color=self.color,
                        color_discrete_map=self.color_discrete_map
                        )

        px_bar.update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            # xaxis_title="FONDEADOR",
            #legend_title="PERFIL DEL CLIENTE",
            font=dict(
                #family="Courier New, monospace",
                size=12,
                color="#fffffc")
        )

        return [dcc.Graph(figure=px_bar)]

    def graphBarPx2(self, *args, **kwargs):
        self.df = kwargs['df']
        self.ejex = kwargs['ejex']
        self.ejey = kwargs['ejey']
        self.title = kwargs['title']
        self.barmode = kwargs['barmode']
        #self.color = kwargs['color']
        #self.color_discrete_map = kwargs['color_discrete_map']
        """
        Elemento grafica de barras (px bar) retornado
        """

        px_bar = px.bar(self.df,
                        x=self.ejex,
                        y=self.ejey,
                        title=self.title,
                        # color=self.color,
                        # color_discrete_map=self.color_discrete_map
                        barmode=self.barmode
                        )

        px_bar.update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            # xaxis_title="FONDEADOR",
            #legend_title="PERFIL DEL CLIENTE",
            font=dict(
                #family="Courier New, monospace",
                size=12,
                color="#fffffc")
        )

        return [dcc.Graph(figure=px_bar)]

#    def graphRadar(self, r, theta):
#        self.r = r
#        self.theta = theta
#
#        fig = go.Figure(data=go.Scatterpolar(
#            r=[1, 5, 2, 2, 3],
#            theta=['processing cost', 'mechanical properties', 'chemical stability', 'thermal stability',
#                   'device integration'],
#            fill='toself'
#        ))

#        fig.update_layout(
#            polar=dict(
#                radialaxis=dict(
#                    visible=True
#                ),
#            ),
#            showlegend=False
#        )

    # TEXTOS

    def drawDescriptionH5(self, text):
        return dbc.Card([html.H5(text)], style={'textAlign': 'center'})

    def drawDescriptionH4(self, text):
        return dbc.Card([html.H4(text)], style={'textAlign': 'center'})

    def drawDescriptionH3(self, text):
        return dbc.Card([html.H3(text)], style={'textAlign': 'center'})

    def drawDescriptionH2(self, text):
        return dbc.Card([html.H2(text)], style={'textAlign': 'center'})

    def drawDescriptionH1(self, text):
        return dbc.Card([html.H1(text)], style={'textAlign': 'center'})

    def drawTitle(self, text):
        return dbc.Card(html.H1(id='h1', className='h1', children=[text], style={'textAlign': 'center',
                                                                                 'color': 'white'}))

    def drawParagraph(self, text, size, color):
        return dbc.Card(html.H6(text,
                                style={
                                    'textAlign': 'center',
                                    'color': color,
                                    'fontSize': size}
                                ))
