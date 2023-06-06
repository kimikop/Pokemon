print ("hey team")
import urllib.request
import json
import requests

offset = 0
endpoint = "https://pokeapi.co/api/v2/"
poke_endpoint = endpoint + "pokemon/"

user_action = True