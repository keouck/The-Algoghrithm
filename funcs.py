import requests
import json

def get_apod_data(api_key, date):
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date').text
    response = json.loads(raw_response)
    return response

def get_image(query):
    raw_response = requests.get(f'https://images-api.nasa.gov/search?q={query}')
    response = json.loads(raw_response)
    return response