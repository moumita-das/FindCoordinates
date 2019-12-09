import json
import requests

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
api_path = os.path.join(dir_path,'google-api-key.txt')
with open(api_path,'r') as file:  # to read the api-key from external file and use it to make the api calls to GeoCode API.
    api_key = file.readline()

if '\n' in api_key:
    api_key = api_key[:api_key.index('\n')]

def find_coordinates(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+address.replace(" " , "+")+'&key='+api_key #for formatting the API call
    response = requests.get(url)
    status = response.status_code
    result = json.loads(response.text) # loading the API response into a json string

    if (status == 200 and result['status']=='OK'): # 1)if call was successful, and 2) result is fetched successfully
        return (result['results'][0]['geometry']['location']['lat'], result['results'][0]['geometry']['location']['lng']) # parse the string to return the lat and lng fields to views.py
    return ("Not Found", " ") 