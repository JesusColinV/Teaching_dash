from dash import dcc
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
import dash_html_components as html


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
                color="#0a0a0a")
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
                color="#0a0a0a")
        )

        return [dcc.Graph(figure=px_bar)]

    # TEXTOS

    def drawDescriptionH5(self, text):
        return html.Div([html.H5(text)], style={'textAlign': 'center'})

    def drawDescriptionH4(self, text):
        return html.Div([html.H4(text)], style={'textAlign': 'center'})

    def drawParagraph(self, text, size, color):
        return html.P(text,
                      style={
                          'textAlign': 'center',
                          'color': color,
                          'fontSize': size}
                      )
