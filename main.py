import requests

token='3d86550455c026ff765791169b598051'

response=requests.post('https://pokemonbattle.me:9104/pokemons', headers={'Content-Type': 'application/json', 'trainer_token' : token},
               json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})
print(response.text)

response_putname = requests.put('https://pokemonbattle.me:9104/pokemons', headers={'Content-Type': 'application/json', 'trainer_token' : token},
               json={
    "pokemon_id": "5996",
    "name": "Gengar",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})
print(response_putname.text)

response_add_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers={'Content-Type': 'application/json', 'trainer_token' : token},
                                      json={
    "pokemon_id": "5996"
})
print(response_add_pokeball.text)