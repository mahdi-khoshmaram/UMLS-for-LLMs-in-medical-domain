import requests, os

def atomResolver(uri):
    ApiKey = os.getenv("UMLS-ApiKey")
    payload = {"language":"ENG","apiKey":ApiKey}
    r = requests.get(uri, params=payload)
    # print(r.url)
    response = r.json()    

    atomsList = response["result"]
    atoms = list()
    for atom in atomsList:
        atomDict = {}
        atomDict["name"] = atom["name"]
        atomDict["AUI"] = atom["ui"]
        atomDict["rootSource"] = atom["rootSource"] 
        atomDict["termType"] = atom["termType"] 
        atomDict["code"] = atom["code"] 
        atomDict["relations"] = atom["relations"] 
        atoms.append(atomDict)
    return atoms


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