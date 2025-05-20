import requests
URL='https://api.pokemonbattle.ru/v2/'
TOKEN='86c7df803f5c009d6061e2757b1d97a1'
HEADER={'content-type':'application/json', 'trainer_token':TOKEN}
body_create={
    "name": "Malyavka",
    "photo_id": 35
}

responce_create=requests.post(url=f'{URL}pokemons', headers=HEADER, json=body_create)
print(responce_create.text)

pokemon_id = responce_create.json()['id']
print(pokemon_id)


import requests
URL='https://api.pokemonbattle.ru/v2/'
TOKEN='86c7df803f5c009d6061e2757b1d97a1'
HEADER={'content-type':'application/json', 'trainer_token':TOKEN}
body_create={
    "pokemon_id": "319074",
    "name": "Pechenka",
    "photo_id": 40
}

responce_create=requests.put(url=f'{URL}pokemons', headers=HEADER, json=body_create)
print(responce_create.text)


import requests
URL='https://api.pokemonbattle.ru/v2/'
TOKEN='86c7df803f5c009d6061e2757b1d97a1'
HEADER={'content-type':'application/json', 'trainer_token':TOKEN}
body_create={
    "pokemon_id": "319905"
}

responce_create=requests.post(url=f'{URL}trainers/add_pokeball', headers=HEADER, json=body_create)
print(responce_create.text)

