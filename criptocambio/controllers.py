from .views import  CriptoView, CriptoViewTK
from .models import CriptoModel
from tkinter import *


'''              
class CriptoControllerTK():

    def __init__(self):
        root = Tk()
        self.vista = CriptoViewTK(root)
        self.modelo = CriptoModelTK()
'''
class CriptoControllerTK(Tk):

    def __init__(self):
        super().__init__()
        self.vista = CriptoViewTK(self, self.calcular_cambio)
        self.modelo = CriptoModel()

    def run(self):
        self.mainloop()

    def calcular_cambio(self):
        #Recoge los datos de la vista
        #Los pasa al modelo
        #Pide conversion al modelo
        #Manda el resultado a vista
        self.modelo.moneda_origen = self.vista.moneda_origen()
        self.modelo.moneda_destino = self.vista.moneda_destino()
        self.modelo.consultar_cambio()

        self.vista.mostrar_cambio(self.modelo.cambio)

        #self.vista.etiqueta_resultado = self.modelo.cambio




class CriptoController:

    def __init__(self):
        self.modelo = CriptoModel()
        self.vista = CriptoView()

    def consultar(self):
        seguir = "S"
        while seguir.upper() == "S":
            desde, hasta = self.vista.pedir_monedas()
            self.modelo.moneda_origen = desde
            self.modelo.moneda_destino = hasta
            self.modelo.consultar_cambio()
            self.vista.mostrar_cambio(desde, hasta, self.modelo.cambio)
            seguir = ""
            while seguir.upper() not in ("S", "N"):
                seguir = input("¿Quieres continuar? (S/N)")