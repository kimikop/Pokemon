import urllib.request
import json
import requests
offset = 0

endpoint_without_offset = "https://pokeapi.co/api/v2/pokemon?limit=10&offset="
user_action = True
new_endpoint = endpoint_without_offset + str(offset)


while user_action:
  response = requests.get(new_endpoint)
  response.raise_for_status()
  data = response.json()
  current_poke = data['results']
  pokes = []
  for pokemon in current_poke:
    poke_name = pokemon['name']
    pokes.append(poke_name)
  print("-----------")
  print(pokes)
  user_action = input("\n\ntype: 'next' to see more pokemon options type: 'pokemon name' to learn more about specific pokemon, type: 'back' to see the previous list of pokemon. type 'stop' to end.\n\n:")
  print("-----------")
  if user_action == "stop":
    user_action = False
    break

  if user_action == "next":
    offset += 10
    new_endpoint = endpoint_without_offset + str(offset)

  elif user_action == "back":
    if (offset > 0):
      offset -= 10
      new_endpoint = endpoint_without_offset + str(offset)
    else: print("You cannot go any further back")

else:
  poke_name = user_action

  for poke in current_poke:
    if poke['name'] == poke_name:
      new_endpoint = poke['url']
      response = requests.get(new_endpoint)
      res = response.json()

      abilities = res['abilities']
      ability_names = []
      for item in abilities:
        ability_obj = item['ability']
        ability_names.append(ability_obj['name'])
      print("Abilities: ", end="")
      print(ability_names)
      print("\n")

new_endpoint = end_point_without_offset + Str(offset)