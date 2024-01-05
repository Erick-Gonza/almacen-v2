import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def create_menu(self, parent):
    menu = ttk.Frame(parent, bootstyle=PRIMARY,
                     width=200, height=650, border=0)
    menu.pack_propagate(0)
    menu.pack(side="left", fill="y", anchor="w")
    ttk.Button(menu, text="Inicio", style="bg.TButton", command=lambda: self.switch_screen(self._home)).pack(
        side="top", fill="x", anchor="center", ipady=5, pady=(16, 0), padx=10)
    ttk.Button(menu, text="Inventario", style="bg.TButton", command=lambda: self.switch_screen(self._inventory)).pack(
        side="top", fill="x", anchor="center", ipady=5, pady=(16, 0), padx=10)
    ttk.Button(menu, text="Entradas", style="bg.TButton", command=lambda: self.switch_screen(self._ins)).pack(
        side="top", fill="x", anchor="center", ipady=5, pady=(16, 0), padx=10)
    ttk.Button(menu, text="Salidas", style="bg.TButton", command=lambda: self.switch_screen(self._outs)).pack(
        side="top", fill="x", anchor="center", ipady=5, pady=(16, 0), padx=10)
    ttk.Button(menu, text="Ordenes", style="bg.TButton", command=lambda: self.switch_screen(self._orders)).pack(
        side="top", fill="x", anchor="center", ipady=5, pady=(16, 0), padx=10)
    # ttk.Button(menu, text="Devoluciones", style="bg.TButton", command=lambda: self.switch_screen(self._returns)).pack(
    #     side="top", fill="x", anchor="center", ipady=5, pady=(16, 0), padx=10)
    ttk.Button(menu, text="Clientes", style="bg.TButton", command=lambda: self.switch_screen(self._clients)).pack(
        side="top", fill="x", anchor="center", ipady=5, pady=(16, 0), padx=10)
    ttk.Button(menu, text="Configuracion", style="bg.TButton", command=lambda: self.switch_screen(self._settings)).pack(
        side="top", fill="x", anchor="center", ipady=5, pady=(16, 0), padx=10)


def create_footer(self):
    footer = ttk.Frame(self, padding=4)
    footer.pack(side="bottom", fill="x")
    ttk.Label(footer, text="Telintec Almacen",
              style="bg.TLabel").pack(side="left", padx=10)
    ttk.Label(footer, text="Version 1.0", style="bg.TLabel").pack(
        side="right", padx=10)
