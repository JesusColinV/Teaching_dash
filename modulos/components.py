from dash import dcc
from datetime import date

class Builder:
    def __init__(self) -> None:
        pass

    def rangePiker(self,*args,**kwargs):
        """
        El elemento input de rango de fechas es retornado
        """
        return  dcc.DatePickerRange(
        id=kwargs['id'],
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2023, 9, 19),
        initial_visible_month=date(2017, 8, 5),
        end_date=date(2017, 8, 25)
        )
        