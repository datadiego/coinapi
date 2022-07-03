#Modelo se ocupa de manejar los datos y llamar a la API
import requests

from criptocambio import APIKEY

class APIError(Exception):
    pass

class CriptoModel:
    def __init__(self):
        self.moneda_origen = ""
        self.moneda_destino = ""
        self.cambio = 0.0

    def consultar_cambio(self):
        headers = {'X-CoinAPI-Key' : APIKEY}
        url = f"http://rest.coinapi.io/v1/exchangerate/{self.moneda_origen}/{self.moneda_destino}"
        respuesta = requests.get(url, headers=headers)
        codigo = respuesta.status_code

        if codigo == 200:
            self.cambio = respuesta.json()["rate"]
        else:
            raise APIError("Ha ocurrido un error {} al consultar la API").format(codigo, respuesta.reason)


class CriptoModelTK():
    pass