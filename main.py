from termResolver import *
from conceptUriResolver import *
from atomResolver import *
from definitionResolver import *
from relationResolver import *

def main(term):

    resultsList = termResolver(term)
    
    for result in resultsList:
        uri = result["uri"]
        resolvedConceptUri = conceptUriResolver(uri)

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
        atoms = atomResolver(resolvedConceptUri["result"]["atoms"])
        concept["atoms"] = atoms 
        # definition
        definitions = definitionResolver(resolvedConceptUri["result"]["definitions"])
        concept["definitions"] = definitions
        # Relations
        relations = relationResolver(resolvedConceptUri["result"]["relations"])
        concept["relations"] = relations


        with open(path, 'w') as jsonFile:
                json.dump(concept, jsonFile, indent=4)
        break
    



main("Naloxone")


