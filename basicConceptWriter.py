import json
import os

# Input: return of term2cui.py 
def basicConceptWriter(resultResults):
    for result in resultResults:
        concept = {
            "name": result["name"],
            "CUI": result["ui"],
            "rootSource": result["rootSource"],
            "ConceptUri": result["uri"],
            "uriOfConceptResolved": False} 

        writeDirectory = "concepts"
        fileName = f"{concept['CUI']}.json"
        conceptsPath = os.path.join(writeDirectory, fileName)
        os.makedirs(writeDirectory, exist_ok=True)

        if not os.path.exists(conceptsPath):
            with open(conceptsPath, 'w') as jsonFile:
                json.dump(concept, jsonFile, indent=4)