import logging
import uuid
import json 
import azure.functions as func



def main(req: func.HttpRequest, outputTable: func.Out[str]) -> func.HttpResponse:
    logging.info('createPage HTTP trigger function processed a request.')

    email = req.params.get('emailaddress')
    rowKey = str(uuid.uuid4())

    if email:
        data = {
            "emailaddress": f"{email}",
            "PartitionKey": "email",
            "RowKey": rowKey

        }

        outputTable.set(json.dumps(data))
        
        return func.HttpResponse(
            f"Subscribed with {email}!",
            status_code=201
        )
    else:
        return func.HttpResponse(
             "Please provide an emailaddress",
             status_code=400
        )
