import requests, os

def AUIofDefaultPreferredAtom(uri):
    ApiKey = os.getenv("UMLS-ApiKey")
    payload = {"apiKey":ApiKey}
    r = requests.get(uri, params=payload)
    # print(r.url)
    response = r.json()    

    AUI = response["result"]["ui"]
    return AUI
