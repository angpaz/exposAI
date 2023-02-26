import logging
import uuid
import json 
import requests 

import os
import openai
import azure.functions as func

def main(req: func.HttpRequest, outputTable: func.Out[str]) -> func.HttpResponse:
    logging.info('createPage HTTP trigger function processed a request.')

    url_gmaps = "https://polite-ocean-0507ce403.2.azurestaticapps.net/api/gmaps?inputprompt=test"
    gmaps_request = requests.request("POST", url_gmaps)
    gmaps_request_res = gmaps_request.text
    input = req.params.get('inputprompt')

    rowKey = str(uuid.uuid4())
    # res = "start"
    errorAI = ""

    api_key = os.environ['openAIKey']
    if input:
        
        try:
            openai.api_key = api_key
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Schreibe ein Expose für eine Wohnung mit folgenden Daten. Unterteile dabei das Ergebnis in Ausstattung (100 Wörter) und Lagebeschreibung (100 Wörter) auf und geben das Ergebnis in diesem json Format aus: result: Ausstattung: , Lage: "+input +". Nutze für die Lagebeschreibung folgende Haltestellen für öffentliche Verkehrsmittel:" + gmaps_request_res ,
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            # stream=True
# sprengletter
# flowfact
# prototyp entwickeln -> makler convention - > preismodell? joint venture?
# klingt nach einem vorschlag
# onoffice
            )
            res = response["choices"][0]["text"]
            # res = response
            data = {
            "inputprompt": f"{input}",
            "output": f"{res}",
            "PartitionKey": "output",
            "RowKey": rowKey
            # "test": json.dumps(res)
            }

            outputTable.set(json.dumps(data))
    
    
            return func.HttpResponse(res, mimetype="text/plain")
        
        except Exception as e:
            errorAI = e
            return func.HttpResponse(
                str(errorAI),
                status_code=201
            )
    else:
        return func.HttpResponse(
             "Please provide an input",
             status_code=400
        )