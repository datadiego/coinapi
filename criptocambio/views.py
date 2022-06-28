#El modelo se comunica con el controlador
#El controlador se comunica con la vista
#El modelo nunca comunica con la vista
class CriptoView:

    def __init__(self):
        pass

    def pedir_monedas(self):
        origen = input("¿Que moneda quieres cambiar?: ")
        destino = input("¿A que moneda quieres cambiar?")
        return (origen, destino)

    def mostrar_cambio(self, origen, destino, cambio):
        print("Un {} vale {:,.2f} en {}".format(origen, cambio, destino))
    