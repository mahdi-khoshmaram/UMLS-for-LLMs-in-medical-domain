import requests

def definitionResolver(ApiKey, uri):
    payload = {"apiKey":ApiKey}
    r = requests.get(uri, params=payload)
    response = r.json()
    # print(r.url)
    definitions = response["result"]  
    defsList = list()
    for definition in definitions:
        defDict = {}
        defDict["rootSource"] = definition["rootSource"]
        defDict["definition"] = definition["value"]
        defsList.append(defDict)
    return defsList
