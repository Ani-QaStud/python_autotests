import requests
import pytest

URL='https://api.pokemonbattle.ru/v2/'
TOKEN='86c7df803f5c009d6061e2757b1d97a1'
HEADER={'content-type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID= '33769'

def test_status_code():
    response=requests.get(url=f'{URL}pokemons', params={'trainer_id':TRAINER_ID})
    assert response.status_code==200

def test_part_of_responce():
    response_get=requests.get(url=f'{URL}trainers/{TRAINER_ID}', params={'trainer_id': TRAINER_ID})
    assert response_get.json()['trainer_name']=="Малинас"
    print(response_get.json())
    