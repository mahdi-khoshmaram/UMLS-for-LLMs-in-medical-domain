import requests
import os

def relationResolver(uri):
    ApiKey = os.getenv("UMLS-ApiKey")
    payload = {"apiKey":ApiKey}

    r = requests.get(uri, params=payload)
    # print(r.url)
    response = r.json()   
    rels = response["result"]
    relList = list()
    for rel in rels:
        relDict = dict()
        relDict["enitity1"] = rel["relatedFromIdName"]
        relDict["enitity2"] = rel["relatedIdName"]
        relDict["relation"] = rel["additionalRelationLabel"]
        relDict["relDescription"] = rel["relationLabel"]
        relDict["entity1Uri"] = rel["relatedFromId"]
        relDict["entity2Uri"] = rel["relatedId"]
        relDict["RUI"] = rel["ui"]
        relDict["rootSource"] = rel["rootSource"]
        relList.append(relDict)
    return relList



