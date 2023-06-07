import urllib.request
import json
import requests

offset = 0
endpoint = "https://pokeapi.co/api/v2/"

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
