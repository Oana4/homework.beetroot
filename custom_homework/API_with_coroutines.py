import requests
import urllib.parse
import asyncio

base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

async def get_response(url):
    return requests.get(url)
    
async def get_coordinates(destination):
    my_key = ''

    safe_destination = urllib.parse.quote(destination)

    full_url = base_url + f'?address={safe_destination}&key={my_key}'

    response = await get_response(full_url)

    try:
        if response.status_code == 200:
            print(f"Yay! You can access {destination}' lat and lng coordinates just with a simple call!\n")
            # print(response.json()['results'][0]['geometry']['location'])
            return response.json()['results'][0]['geometry']['location']
        else:
            print(f"Your status code is {response.status_code}")
    except Exception as err:
        print(err)


async def main():
    results = await asyncio.gather(
        get_coordinates("Paris"),
        get_coordinates("London"),
        get_coordinates("Tokyo")
    )
    print(results)


asyncio.run(main())
