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
  pokes = []
  for pokemon in current_poke:
    poke_name = pokemon['name']
    pokes.append(poke_name)
    print("----------")
    print(pokes)
    user _action = input("\n\ntype: 'next' to see more pokemon opptions type: 'pokemon name' to learn more about specific pokemon, type: 'back' to see the previous list of pokemon. type 'stop' to end.\n\n:")
    print("-----------")
    if user_action == "stop":
  user_action = False
  break

if user_action == "next":
  offset += 10
  new_endpoint = endpoint_without_offset + str(offset)

elif user_action == "back":
  if (offset > 0):
    offset += 10
    new_endpoint = endpoint_without_offset + str(offset)
  else: print("You cannot go any further back")
    