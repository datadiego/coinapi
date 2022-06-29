import requests

url = "http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

draw = "https://deckofcardsapi.com/api/deck/baraja_id/draw/?count=2"
respuesta = requests.get(url)
respuesta_json = respuesta.json()


baraja_id = respuesta_json["deck_id"]
draw = "https://deckofcardsapi.com/api/deck/"+baraja_id+"/draw/?count=2"

x = requests.get(draw)
for elementos in x:
    print(elementos)

