print ("hey team")
import urllib.request
import json
import requests

offset = 0
endpoint = "https://pokeapi.co/api/v2/"
poke_endpoint = endpoint + "pokemon/"
offset_poke_endpoint_fun = lambda offset: poke_endpoint + "?offset={}&limit=10".format(offset)
new_endpoint = offset_poke_endpoint_fun(offset)

user_action = True

while user_action:
  