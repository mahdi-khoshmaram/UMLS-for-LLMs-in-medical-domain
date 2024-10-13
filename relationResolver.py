import requests

def relationResolver(ApiKey, uri):
    payload = {
        "apiKey":ApiKey
        }
    r = requests.get(uri, params=payload)
    # print(r.url)
    response = r.json()    