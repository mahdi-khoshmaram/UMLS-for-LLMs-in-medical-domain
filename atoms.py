import requests

def atoms(ApiKey, uri):
    payload = {"language":"ENG","apiKey":ApiKey}
    r = requests.get(uri, params=payload)
    print(r.url)
    response = r.json()    
    return response["result"]


#return sample
# {
#       "classType": "Atom",
#       "ui": "A0484452",
#       "sourceDescriptor": "NONE",
#       "sourceConcept": "NONE",
#       "concept": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C0027358",
#       "suppressible": "false",
#       "obsolete": "false",
#       "rootSource": "AOD",
#       "termType": "DE",
#       "code": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/source/AOD/0000020562",
#       "language": "ENG",
#       "name": "naloxone",
#       "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/AUI/A0484452/ancestors",
#       "descendants": "NONE",
#       "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/AUI/A0484452/attributes",
#       "relations": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/AUI/A0484452/relations",
#       "children": "NONE",
#       "parents": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/AUI/A0484452/parents"
#     },