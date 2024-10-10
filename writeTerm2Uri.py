import json
import os

# Input: return of term2cui.py 
def writeTerm2Uri(results):
    for result in results:
        concept = {
            "name": result["name"],
            "ui": result["ui"],
            "rootSource": result["rootSource"],
            "uri": result["uri"]
        } 

        writeDirectory = "concepts"
        fileName = f"{concept['ui']}.json"
        path = os.path.join(writeDirectory, fileName)
        os.makedirs(writeDirectory, exist_ok=True)

        if os.path.exists(path):
            print(f"The file [{fileName}] exists in [{path}]!")

        if not os.path.exists(path):
            with open(path, 'w') as jsonFile:
                json.dump(concept, jsonFile, indent=4)
                print(f"{fileName} has been written.")
