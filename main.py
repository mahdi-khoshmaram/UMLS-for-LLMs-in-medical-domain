from termResolver import *
from conceptUriResolver import *
from atomResolver import *

def main(term):
    ApiKey = input("Enter UMLS APIKEY: ")
    resultsList = termResolver(ApiKey, term)
    
    for result in resultsList:
        uri = result["uri"]
        resolvedConceptUri = conceptUriResolver(ApiKey, uri)

        # Read the concept basic information from ./concepts dir
        writeDirectory = "concepts"
        fileName = f"{resolvedConceptUri["result"]['ui']}.json"
        path = os.path.join(writeDirectory, fileName)
        os.makedirs(writeDirectory, exist_ok=True)
        with open(path, "r") as jsonFile:
            concept = json.load(jsonFile)

        concept["uriOfConceptResolved"] = True

        # resolvedConceptUri["result"]["semanticTypes"] is LIST OF DICTIONARIES!
        concept["semanticTypes"] = resolvedConceptUri["result"]["semanticTypes"] 
        
        # atoms 
        resolvedAtom = atomResolver(ApiKey, resolvedConceptUri["result"]["atoms"])
        print(resolvedAtom)
        break
        atomsList = resolvedAtom["result"]
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
        
        concept["atoms"] = atoms 
        with open(path, 'w') as jsonFile:
                json.dump(concept, jsonFile, indent=4)
        break
    



main("Naloxone")


