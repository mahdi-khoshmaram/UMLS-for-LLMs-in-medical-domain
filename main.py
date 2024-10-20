from termResolver import *
from conceptUriResolver import *
from atomResolver import *
from definitionResolver import *
from relationResolver import *
from AUIofDefaultPreferredAtom import *


def main(term):
    termResolved = termResolver(term)
    concepts = termResolved["result"]["results"]
    
    i = 1
    for Concept in concepts:
        uri = Concept["uri"]
        resolvedConceptUri = conceptUriResolver(uri)

        # Reading the concept basic information from ./concepts dir
        writeDirectory = "concepts"
        fileName = f"{resolvedConceptUri["result"]['ui']}.json"
        path = os.path.join(writeDirectory, fileName)
        os.makedirs(writeDirectory, exist_ok=True)
        with open(path, "r") as jsonFile:
            concept = json.load(jsonFile)
        if concept["uriOfConceptResolved"] == True:
            print(f"---- The concept: {resolvedConceptUri["result"]['ui']}.json has been fetched already ----")
            i += 1
            continue


        print(f"--- {resolvedConceptUri["result"]['ui']} is receiving from UMLS ---")
        
        concept["uriOfConceptResolved"] = True

        # Semantic
        concept["semanticTypes"] = resolvedConceptUri["result"]["semanticTypes"] 
        print("-- [semanticTypes] fetched --")


        # atoms
        atoms = atomResolver(resolvedConceptUri["result"]["atoms"])
        concept["atoms"] = atoms 
        print("-- [atoms] fetched --")


        # definition
        definitionsURI = resolvedConceptUri["result"]["definitions"]
        if not definitionsURI == "NONE":
            definitions = definitionResolver(definitionsURI)
            concept["definitions"] = definitions
            print("-- [definitions] fetched --")
        else: 
            concept["definitions"] = "NONE"
            print("-- [definitions] = NONE --")


        # Relations
        relationURI = resolvedConceptUri["result"]["relations"]
        if not relationURI == "NONE":
            relations = relationResolver(relationURI)
            concept["relations"] = relations
            print("-- [relations] fetched --")
        else:
             concept["relations"] = "NONE"
             print("-- [relations] = NONE -- \n")

             
        # defaultPreferredAtom
        AUIofPreferred = AUIofDefaultPreferredAtom(resolvedConceptUri["result"]["defaultPreferredAtom"])
        for atom in concept["atoms"]:
             if atom["AUI"] == AUIofPreferred:
                  atom["defaultPreferredAtom"] = True

                  
        with open(path, 'w') as jsonFile:
                json.dump(concept, jsonFile, indent=4)
        i += 1

    



main("Naloxone")


