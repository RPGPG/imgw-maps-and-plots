import requests
import json

data = requests.get("https://danepubliczne.imgw.pl/api/data/synop/")
json_data = data.json()
file_json = open("/home/python-runner/data/twp.json", "w")
file_json.write(json.dumps(json_data))
