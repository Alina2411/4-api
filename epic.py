import requests
import os
import datetime
from downloads_images import downloads_images

def fetch_nasa_epic():
    nasa_token = '2pzXEr6S459lIrdI9Ndw0oz5MAFnt2aFfCwuMit2'
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural/image'
    params ={
        'api_key': nasa_token,
        'count': 30
    }
    response = requests.get(nasa_epic_url, params=params)
    epic_image = response.json()
    for image in epic_image:
      epic_name = image['image']
      epic_date = image['date']
      epic_date = datetime.datetime.fromisoformat(epic_date).strftime('%Y/%m/%d')                
      epic_url= f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_name}.png'
      path = os.path.join('images',f'{epic_name}.png')
      downloads_images(path, epic_url, params)


def main():
    fetch_nasa_epic()

if __name__ == '__main__':
    main()