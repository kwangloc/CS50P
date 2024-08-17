# request library to make HTTP requests
import requests
# sys library to use command-line arguments 
import sys
# json library to manipulate JSON data
import json
    
if len(sys.argv) != 2:
    sys.exit

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(response.json())
# print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o["results"]:
    print(result["trackName"])
