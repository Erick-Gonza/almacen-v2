from PIL import Image
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.widgets import *
from src.controllers.index import DataHandler
Image.CUBIC = Image.BICUBIC


class HomeScreen(ttk.Frame):
    def __init__(self):
        ttk.Frame.__init__(self, style="bg.TFrame")
        self.pack(side="top", fill="both", expand=True)
        self._data = DataHandler()
        self._total_profit = self._data._order.get_profit()
        self._total_orders = len(self._data._order.get_all_orders())
        self._total_returns = 0
        self.create_content(self)

    def create_content(self, parent):
        '''Creates the content of the home screen, includes only graphics charts'''
        content = ttk.Frame(parent, style="bg.TFrame")
        content.pack(side="left", fill="both", expand=True)
        ttk.Label(content, text="Inicio", style="bg.TLabel", font=(
            "Arial Black", 25)).pack(
            side="top", fill="x", anchor="center", ipady=5, pady=(16, 0), padx=10)

        # Graphics 1row 3 columns on center
        graphics = ttk.Frame(content, style="bg.TFrame")
        graphics.place(anchor="c", relx=.5, rely=.5)

        # chart 1
        chart_profit = ttk.Meter(
            graphics,
            metersize=300,
            bootstyle="success",
            amountused=self._total_profit[0][0],
            amounttotal='500000',
            textleft='$',
            metertype="full",
            padding=10,
            stripethickness=10,
            subtext="Ingresos"
        )
        chart_profit.pack(side="left", fill="both", expand=True, padx=10)

        # chart 2
        chart_orders = ttk.Meter(
            graphics,
            metersize=300,
            bootstyle="info",
            amountused=self._total_orders,
            amounttotal='500000',
            textleft='$',
            metertype="full",
            padding=10,
            stripethickness=10,
            subtext="Pedidos"
        )
        chart_orders.pack(side="left", fill="both", expand=True, padx=10)

        # chart 3
        chart_returns = ttk.Meter(
            graphics,
            metersize=300,
            bootstyle="danger",
            amountused=0,
            amounttotal='500000',
            textleft='$',
            metertype="full",
            padding=10,
            stripethickness=10,
            subtext="Devoluciones"
        )
        chart_returns.pack(side="left", fill="both", expand=True, padx=10)

        # Chart 4
        chart_profit = ttk.Meter(
            graphics,
            metersize=300,
            bootstyle="success",
            amountused=0,
            amounttotal='500000',
            textleft='$',
            metertype="full",
            padding=10,
            stripethickness=10,
            subtext="Ingresos"
        )
        chart_profit.pack(side="left", fill="both", expand=True, padx=10)
