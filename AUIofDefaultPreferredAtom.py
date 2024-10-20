import requests, os

def AUIofDefaultPreferredAtom(uri):
    ApiKey = os.getenv("UMLS-ApiKey")
    payload = {"apiKey":ApiKey}
    r = requests.get(uri, params=payload)
    response = r.json()    

    AUI = response["result"]["ui"]
    return AUI

# AUIofDefaultPreferredAtom("https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C0027358/atoms/preferred")

# response Sample
# {
#   "pageSize": 25,
#   "pageNumber": 1,
#   "pageCount": 1,
#   "result": {
#     "classType": "Atom",
#     "ui": "A31563199",
#     "sourceDescriptor": "NONE",
#     "sourceConcept": "NONE",
#     "concept": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C0027358",
#     "suppressible": "false",
#     "obsolete": "false",
#     "rootSource": "MTH",
#     "termType": "PN",
#     "code": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/source/MTH/NOCODE",
#     "language": "ENG",
#     "name": "naloxone",
#     "ancestors": "NONE",
#     "descendants": "NONE",
#     "attributes": "NONE",
#     "relations": "NONE",
#     "children": "NONE",
#     "parents": "NONE"
#   }
# }