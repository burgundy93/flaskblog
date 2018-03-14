import requests
import json

url ="http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=ronald911&api_key=b45188c880a0f2f08c244f72d92d011d&format=json"

r = requests.get(url)

raw = r.json()

data = json.dumps(raw["recenttracks"])

loaded = json.loads(data)
