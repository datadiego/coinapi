#El modelo se comunica con el controlador
#El controlador se comunica con la vista
#El modelo nunca comunica con la vista
import tkinter
from tkinter import ttk
from . import monedas   

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
        super().__init__(padre, width = 400, height = 400, padding = 20)
        self.grid()
        self.crear_controles()
        

    def crear_controles(self):
        #Entrada moneda origen
        etiqueta_entrada = ttk.Label(self, text="Moneda de origen")
        etiqueta_entrada.grid(row = 0, column = 0)

        combo_entrada = ttk.Combobox(self, values = monedas)
        combo_entrada.grid(row = 1, column = 0)

        
        #Entrada moneda destino
        etiqueta_destino = ttk.Label(self, text = "Moneda de destino")
        etiqueta_destino.grid(row = 0, column = 1)
        
        combo_destino = ttk.Combobox(self, values = monedas)
        combo_destino.grid(row = 1, column = 1)
        
        #Etiqueta de resultado
        self.etiqueta_resultado = ttk.Label(self, text="0.0", padding = 20)
        self.etiqueta_resultado.grid(row = 2, column = 0, columnspan=2)

        self.boton_calcular = ttk.Button(self, text = "Calcular")
        self.boton_calcular.grid(row = 3, column = 1)