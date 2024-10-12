import requests

def conceptUriResolver(ApiKey, uri):
    payload = {"apiKey":ApiKey}
    r = requests.get(uri, params=payload)
    response = r.json()    
    return response


# return sample:
    # {
    # "pageSize": 25,
    # "pageNumber": 1,
    # "pageCount": 1,
    # "result": {
    #     "ui": "C0027358",
    #     "name": "naloxone",
    #     "dateAdded": "09-30-1990",
    #     "majorRevisionDate": "04-29-2021",
    #     "classType": "Concept",
    #     "suppressible": false,
    #     "status": "R",
    #     "semanticTypes": [
    #     {
    #         "name": "Organic Chemical",
    #         "uri": "https://uts-ws.nlm.nih.gov/rest/semantic-network/2024AA/TUI/T109"
    #     }
    #     ],
    #     "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C0027358/atoms",
    #     "definitions": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C0027358/definitions",
    #     "relations": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C0027358/relations",
    #     "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C0027358/atoms/preferred",
    #     "atomCount": 69,
    #     "cvMemberCount": 0,
    #     "attributeCount": 0,
    #     "relationCount": 19
    # }
    # }