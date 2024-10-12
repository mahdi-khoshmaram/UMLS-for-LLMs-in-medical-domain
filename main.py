from termResolver import *
from conceptUriResolver import *
from atomResolver import *
from definitionResolver import *

def main(term):
    ApiKey = "265c7e4c-c500-4c9b-8333-3e42832bea1b"
    # ApiKey = input("Enter UMLS APIKEY: ")
    resultsList = termResolver(ApiKey, term)
    
    for result in resultsList:
        uri = result["uri"]
        resolvedConceptUri = conceptUriResolver(ApiKey, uri)

        # Reading the concept basic information from ./concepts dir
        writeDirectory = "concepts"
        fileName = f"{resolvedConceptUri["result"]['ui']}.json"
        path = os.path.join(writeDirectory, fileName)
        os.makedirs(writeDirectory, exist_ok=True)
        with open(path, "r") as jsonFile:
            concept = json.load(jsonFile)
        if concept["uriOfConceptResolved"] == True:
            print("Resolved Already!")
            # break

        concept["uriOfConceptResolved"] = True
        # Semantic
        concept["semanticTypes"] = resolvedConceptUri["result"]["semanticTypes"] 
        # atoms
        atoms = atomResolver(ApiKey, resolvedConceptUri["result"]["atoms"])
        concept["atoms"] = atoms 
        # definition
        definitions = definitionResolver(ApiKey, resolvedConceptUri["result"]["definitions"])
        concept["definitions"] = definitions


        with open(path, 'w') as jsonFile:
                json.dump(concept, jsonFile, indent=4)
        break
    



main("Naloxone")


