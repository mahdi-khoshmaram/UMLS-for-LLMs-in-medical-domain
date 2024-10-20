import requests, os
from basicConceptWriter import *

def termResolver(term):
    ApiKey = os.getenv("UMLS-ApiKey")
    
    # build a directoty to save the searched terms in a json format 
    writeDirectory = "savedTerms"
    fileName = "terms.json"
    savedTermsPath = os.path.join(writeDirectory, fileName)
    os.makedirs(writeDirectory, exist_ok=True)



    # tries to read the json file of searched terms, else create a temporary terms dict
    try:
        with open(savedTermsPath, "r") as readFile:
            terms = json.load(readFile)
    except FileNotFoundError:
         terms = dict()
    

    # If I found term in the json file of searched terms, script will not conncet to the API
    if term in terms.keys():
        print(f"----- The term: [{term}] resolved to its concepts OFFLINE -----")
        return terms[term]
    

    if term not in terms.keys():
        searchType = "words"
        pageNumber = 1
        pageSize = 5
        payload = {"string":term, "pageNumber":pageNumber, "searchType":searchType, "pageSize":pageSize, "apiKey":ApiKey}
        r = requests.get('https://uts-ws.nlm.nih.gov/rest/search/current', params=payload)
        response = r.json()

        
        # saving each concept
        resultResults = response["result"]["results"]
        basicConceptWriter(resultResults)

        # log
        terms[term] = response
        with open(savedTermsPath, 'a') as jsonFile:
            json.dump(terms, jsonFile, indent=4)
        print("----- The term: [{term}] resolved to its concepts ONLINE -----")
        return response
    


# a = termResolver("Naloxone")
# print(a)