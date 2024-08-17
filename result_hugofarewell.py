import requests
import json

with open('hugofarewell.txt', 'r', encoding='utf8') as file:
    json_data = file.read()
try:
    data_dict = json.loads(json_data)
    for token in data_dict:
        try:
            print(f"😀 name: {data_dict[token]['name']}")
        except KeyError:
            pass
        try:
            print(f"bestEvents: {data_dict[token]['bestEvents']['answer']}")
        except KeyError:
            pass
        try:
            print(f"bestMembers: {data_dict[token]['bestMembers']['answer']}")
        except KeyError:
            pass
        try:
            print(f"perfectDuos: {data_dict[token]['perfectDuos']['answer']}")
        except KeyError:
            pass
        try:
            print(f"theRookies: {data_dict[token]['theRookies']['answer']}")
        except KeyError:
            pass
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")



# print(json.dumps(response.json(), indent=2))
# json_str = json.dumps(response.json(), ensure_ascii=False).encode('utf8')
# print(json_str.decode())
# with open('json.txt', 'w', encoding='utf8') as json_str:
#     json.dump(response.json(), json_str, ensure_ascii=False)
# o = response.json()
# for result in o["results"]:
#     print(result["trackName"])