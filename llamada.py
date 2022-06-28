import requests

apikey = "22F13E69-3D63-40A2-A70B-556821A8CE07"
api_url = "http://rest.coinapi.io"
endpoint = "/v1/assets"

headers = {'X-CoinAPI-Key' : apikey}
url = api_url + endpoint

respuesta = requests.get(url, headers=headers)
codigo = respuesta.status_code

if codigo == 200:
    print("El resultado de la consulta es:")
    respuesta_json = respuesta.json()

    for moneda in respuesta_json:
        if moneda["asset_id"].startswith("EUR"):
            print(moneda["name"])
        #print(moneda["name"], moneda["asset_id"])
else:
    print("La peticion a la API ha fallado")
    print(f"Código del error {codigo}")
    print(f"Razon del error: {respuesta.reason}")
    print(respuesta.text)