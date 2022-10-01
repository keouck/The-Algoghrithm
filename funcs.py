import requests
import json

def get_apod_data(api_key):
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}').text
    response = json.loads(raw_response)
    return response

def get_neows_data(start_date, end_date, api_key):
    raw_response = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}').text
    response = json.loads(raw_response)
    return response
