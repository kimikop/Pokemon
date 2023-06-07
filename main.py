print ("hey team")
import urllib.request
import json
import requests

offset = 0
endpoint_without_offset = "https://pokeapi.co/api/v2/pokemon?limit=10&offset="
user_action = True
new_endpoint = endpoint_without_offset + str(offset)

while user_action:
  response = requests.get(new_endpoint)
  data = response.json()
  cuurent_poke = data['results']