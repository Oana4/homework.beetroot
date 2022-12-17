import requests
import urllib.parse

my_key = ''

base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

destination = 'Paris'

safe_destination = urllib.parse.quote(destination)

full_url = base_url + f'?address={safe_destination}&key={my_key}'

print(full_url)

response = requests.get(full_url)

try:
    if response.status_code == 200:
        print("Yay! You can access Paris' lat and lng coordinates just with a simple call!\n")
        print(response.json()['results'][0]['geometry']['location'])
    else:
        print(f"Your status code is {response.status_code}")
except Exception as err:
    print(err)
