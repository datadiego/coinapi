import requests

apikey = "22F13E69-3D63-40A2-A70B-556821A8CE07"

headers = {'X-CoinAPI-Key' : apikey}

seguir = "S"
while seguir == "S":
    moneda_origen = input("¿Que moneda quieres cambiar?: ")
    moneda_destino = input("¿A que moneda quieres cambiar?")
    url = f"http://rest.coinapi.io/v1/exchangerate/{moneda_origen}/{moneda_destino}"

    respuesta = requests.get(url, headers=headers)

    tipo_cambio = respuesta.json()
    cambio = tipo_cambio["rate"]

    print("Un {} vale {:,.2f} en {}".format(moneda_origen, cambio, moneda_destino))

    seguir = ""
    while seguir.upper() not in ("S", "N"):
        seguir = input("¿Quieres continuar? (S/N)")


