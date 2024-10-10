from term2cui import *
from uri2info import *
from atoms import *

def main(term):
    ApiKey = input("Enter UMLS APIKEY: ")
    resultsList = term2cui(ApiKey, term)
    
    for result in resultsList:
        uri = result["uri"]
        uriInfo = uri2info(ApiKey, uri)
        atomsList = atoms(ApiKey, uriInfo["result"]["atoms"])
        atoms = {}
        for atom in atomsList:
            atoms["name"] = atom["name"]
            atoms["rootSource"] = atom["rootSource"] 

        writeDirectory = "concepts"
        fileName = f"{uriInfo["result"]['ui']}.json"
        path = os.path.join(writeDirectory, fileName)
        os.makedirs(writeDirectory, exist_ok=True)

        with open(path, "r") as jsonFile:
            concept = json.load(jsonFile)
        
        concept["mappedUri"] = True
        concept["semanticTypes"] = uriInfo["result"]["semanticTypes"]
        concept["atoms"] = atoms
        
        print(atomsList)

        break
    



main("Naloxone")


