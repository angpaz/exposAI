import logging
import uuid
import json 

import os
import openai
import azure.functions as func


import googlemaps


def main(req: func.HttpRequest, outputTable: func.Out[str]) -> func.HttpResponse:
    logging.info('createPage HTTP trigger function processed a request.')

    input = req.params.get('inputprompt')

    rowKey = str(uuid.uuid4())
    # res = "start"

    # api_key = os.environ['openAIKey']
    if input:
        
        try:
            # Ersetzen Sie den Platzhalter YOUR_API_KEY durch Ihren eigenen API-Schlüssel
            gmaps = googlemaps.Client(key='AIzaSyCZ2PJjy3w7PHG1WOjbEiD3dbxL07qhwQY')

            # Geben Sie die gewünschte Adresse ein
            address = 'Auf dem Römerberg 21, 50968 Köln'

            # Rufen Sie die Geocoding-API auf, um die Koordinaten zu erhalten
            geocode_result = gmaps.geocode(address)

            # Extrahieren Sie die Koordinaten aus der API-Antwort
            lat = geocode_result[0]['geometry']['location']['lat']
            lng = geocode_result[0]['geometry']['location']['lng']


            # from geopy.distance import distance

            # Rufen Sie die Places API auf, um die nächstgelegenen Stationen zu finden
            places_result = gmaps.places_nearby(
                location=(lat, lng),
                keyword="nächste Haltestelle",
                rank_by="distance"
            )

            # Extrahieren Sie die Koordinaten der Stationen aus der API-Antwort
            # station_locations = [
            #     (place['geometry']['location']['lat'], place['geometry']['location']['lng'], place['name'])
            #     for place in places_result['results']
            # ]

            station_locations = [
                (place['name'])
                for place in places_result['results']
            ]
        
            station_locations=station_locations[0:3]

            # outputTable.set(json.dumps(station_locations))
    
    
            return func.HttpResponse(json.dumps(station_locations,ensure_ascii=False), mimetype="text/plain")
        
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