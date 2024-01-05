import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.widgets import *
from src.screens.Home import HomeScreen
from src.screens.Clients import ClientsScreen
from src.screens.Settings import SettingsScreen
from src.screens.In import InScreen
from src.screens.Out import OutScreen
from src.screens.Inventory import InventoryScreen
from src.screens.Orders import OrdersScreen
from src.screens.Returns import ReturnsScreen


class App(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Telintec Almacen")
        self.geometry("500x500")
        self.resizable(True, True)
        self.after(0, lambda: self.state('zoomed'))
        self.place_window_center()
        self._current_frame = None
        self._home = HomeScreen
        self._clients = ClientsScreen
        self._settings = SettingsScreen
        self._ins = InScreen
        self._outs = OutScreen
        self._inventory = InventoryScreen
        self._orders = OrdersScreen
        self._returns = ReturnsScreen

        ttk.Style().configure("primary.TFrame",
                              background="#04053A",
                              foreground="white",
                              bordercolor="#04053A",
                              lightcolor="#04053A",
                              darkcolor="#04053A",
                              padding=4)
        ttk.Style().configure("TButton", font=(
            "Segoe UI", 10), padding=6, bordercolor="#04053A", borderwidth=2)

        create_menu(self, self)
        self.switch_screen(self._home)
        create_footer(self)

    def switch_screen(self, new_frame):
        if self._current_frame:
            self._current_frame.pack_forget()
        self._current_frame = new_frame()
