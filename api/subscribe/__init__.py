import logging
import uuid
import json 

import os
import openai
import azure.functions as func

def main(req: func.HttpRequest, outputTable: func.Out[str]) -> func.HttpResponse:
    logging.info('createPage HTTP trigger function processed a request.')

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
            prompt="Schreibe ein Expose für eine Wohnung mit folgenden Daten. Unterteile dabei das Ergebnis in Ausstattung und Lagebeschreibung auf und gebe das Ergebnis im json Format aus."+input,
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            # stream=True

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