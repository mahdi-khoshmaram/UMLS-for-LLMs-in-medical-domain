import requests, os

def definitionResolver(uri):
    ApiKey = os.getenv("UMLS-ApiKey")
    payload = {"apiKey":ApiKey}
    r = requests.get(uri, params=payload)
    response = r.json()
    
    definitions = response["result"]
    defsList = list()
    for definition in definitions:
        defDict = {}
        defDict["rootSource"] = definition["rootSource"]
        defDict["definition"] = definition["value"]
        defsList.append(defDict)
    return defsList


# definitionResolver("https://uts-ws.nlm.nih.gov/rest/content/2024AA/CUI/C0027358/definitions")


# response Sample
# {
#   "pageSize": 25,
#   "pageNumber": 1,
#   "pageCount": 1,
#   "result": [
#     {
#       "rootSource": "MSHPOR",
#       "value": "Antagonista específico de ópio sem atividade agonista. É um antagonista competitivo dos receptores opioides mu, delta e kappa.",
#       "classType": "Definition",
#       "sourceOriginated": true
#     },
#     {
#       "rootSource": "CSP",
#       "value": "specific opiate antagonist with no agonist activity, a competitive antagonist at mu, delta, and kappa opioid receptors.",
#       "classType": "Definition",
#       "sourceOriginated": true
#     },
#     {
#       "rootSource": "MSH",
#       "value": "A specific opiate antagonist that has no agonist activity. It is a competitive antagonist at mu, delta, and kappa opioid receptors.",
#       "classType": "Definition",
#       "sourceOriginated": true
#     },
#     {
#       "rootSource": "NCI",
#       "value": "A thebaine derivate with competitive opioid antagonistic properties. Naloxone reverses the effects of opioid analgesics by binding to the opioid receptors in the CNS, and inhibiting the typical actions of opioid analgesics, including analgesia, euphoria, sedation, respiratory depression, miosis, bradycardia, and physical dependence. Naloxone binds to mu-opioid receptors with a high affinity, and a lesser degree to kappa- and gamma-opioid receptors in the CNS.",
#       "classType": "Definition",
#       "sourceOriginated": true
#     },
#     {
#       "rootSource": "MSHSPA",
#       "value": "Un antagonista específico del opio que no tiene actividad agonista. Es un antagonista competitivo en los receptores opioides mu, delta y kappa.",
#       "classType": "Definition",
#       "sourceOriginated": true
#     },
#     {
#       "rootSource": "MSHSWE",
#       "value": "Ett antagonistiskt opiat utan någon agonistverkan. Det är en kompetitiv antagonist på mu-, delta- och kappa-opioidreceptorer.",
#       "classType": "Definition",
#       "sourceOriginated": true
#     }
#   ]
# }