from dash import dcc
from datetime import date
import plotly.express as px
import plotly.graph_objects as go


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

#df, ejex, ejey, title='Titulo de la grafica'
    def graphBarPx(self, *args, **kwargs):
        self.df = kwargs['df']
        self.ejex = kwargs['ejex']
        self.ejey = kwargs['ejey']
        self.title = kwargs['title']
        """
        Elemento grafica de barras (px bar) retornado
        """

        px_bar = px.bar(self.df,
                        x=self.ejex,
                        y=self.ejey,
                        title=self.title)
        px_bar.update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
        )

        return [dcc.Graph(figure=px_bar)]


'''
    def graphBarPxGrouped(self, df, ejex, ejey, title='Titulo de la grafica', barmode='group'):
        """
        Elemento grafica de barras (px bar) retornado
        """

        px_bar = px.bar(df,
                        x=ejex,
                        y=ejey,
                        barmode=barmode,
                        title=title)
        px_bar.update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
        )

        return px_bar

    def graphBarPxColor(self, df, ejex, ejey, color, title='Titulo de la grafica'):
        """
        Elemento grafica de barras (px bar) retornado
        """

        px_bar = px.bar(df,
                        x=ejex,
                        y=ejey,
                        color=color,
                        title=title)
        px_bar.update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
        )

        return px_bar
'''
