import requests
from writeTerm2Uri import *

def term2cui(ApiKey, term):
    
    # build a directoty to save the searched terms in a json format 
    writeDirectory = "savedTerms"
    fileName = "terms.json"
    path = os.path.join(writeDirectory, fileName)
    os.makedirs(writeDirectory, exist_ok=True)

    # tries to read the json file of searched terms, else create a temporary terms dict
    try:
        with open(path, "r") as readFile:
            terms = json.load(readFile)
    except FileNotFoundError:
         terms = dict()
    
    # If I found term in the json file of searched terms, script will not conncet to the API
    if term in terms.keys():
        print("returned from the json file...")
        return terms[term]["result"]["results"]
    

    # esle it will fetch information by connecting to the API
    if term not in terms.keys():
        # ‘exact’,‘words’,‘leftTruncation’, ‘rightTruncation’, ‘normalizedString’, ‘normalizedWords’
        # searchType = "normalizedString"
        searchType = "words"
        pageNumber = 1
        pageSize = 5

        # fetch data
        payload = {"string":term, "pageNumber":pageNumber, "searchType":searchType, "pageSize":pageSize, "apiKey":ApiKey}
        r = requests.get('https://uts-ws.nlm.nih.gov/rest/search/current', params=payload)
        response = r.json()

        # log
        terms[term] = response
        with open(path, 'a') as jsonFile:
            json.dump(terms, jsonFile, indent=4)
            # print(f"Term {term} logged!")
        print("returned from the UMLS API...")
        print(f"Term {term} logged!")
        return response["result"]["results"]
    



# return sample:
# "results": [
#                 {
#                     "ui": "C0027358",
#                     "rootSource": "MTH",
#                     "uri": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C0027358",
#                     "name": "naloxone"
#                 },
#                 {
#                     "ui": "C0700549",
#                     "rootSource": "MTH",
#                     "uri": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C0700549",
#                     "name": "naloxone hydrochloride"
#                 },
#                 {
#                     "ui": "C0717936",
#                     "rootSource": "RXNORM",
#                     "uri": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C0717936",
#                     "name": "naloxone / pentazocine"
#                 },
#                 {
#                     "ui": "C1169989",
#                     "rootSource": "RXNORM",
#                     "uri": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C1169989",
#                     "name": "buprenorphine / naloxone"
#                 },
#                 {
#                     "ui": "C3848704",
#                     "rootSource": "RXNORM",
#                     "uri": "https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C3848704",
#                     "name": "naloxone / oxycodone"
#                 }
#             ]