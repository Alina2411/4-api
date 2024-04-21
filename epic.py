import requests
import os
import datetime
from download_image import download_image


def fetch_nasa_epic(nasa_token):
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural/image'
    count = 30
    params ={
        'api_key': nasa_token,
        'count': count
    }
    response = requests.get(nasa_epic_url, params=params)
    epic_images = response.json()
    for image in epic_image:
      epic_name = image['image']
      epic_date = image['date']
      epic_date = datetime.datetime.fromisoformat(epic_date).strftime('%Y/%m/%d')                
      epic_url= f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_name}.png'
      path = os.path.join('images',f'{epic_name}.png')
      download_image(path, epic_url, params)


def main():
    nasa_token = os.environ['NASA_TOKEN']
    fetch_nasa_epic(nasa_token)


if __name__ == '__main__':
    main()
