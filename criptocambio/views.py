#El modelo se comunica con el controlador
#El controlador se comunica con la vista
#El modelo nunca comunica con la vista
import tkinter
from tkinter import ttk

class CriptoView:

    def __init__(self):
        pass

    def pedir_monedas(self):
        origen = input("¿Que moneda quieres cambiar?: ")
        destino = input("¿A que moneda quieres cambiar?")
        return (origen, destino)

    def mostrar_cambio(self, origen, destino, cambio):
        print("Un {} vale {:,.2f} en {}".format(origen, cambio, destino))

class CriptoViewTK(ttk.Frame):
    def __init__(self, padre):
        super().__init__(padre, width = 400, height = 400)
        self.grid()
        self.crear_controles()
        

    def crear_controles(self):
        label = ttk.Label(self, text="Criptocambio")
        label.grid(row=0, column=0)
