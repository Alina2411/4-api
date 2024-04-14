import requests
import os
from urllib.parse import urlparse, unquote
from download_image import download_image


def get_extension(url):
    decoded_url = unquote(url)
    parsed_url = urlparse(decoded_url)
    path, fullname = os.path.split(parsed_url.path)
    file_name, extension = os.path.splitext(fullname)
    return extension, file_name


def fetch_nasa_apod(nasa_token):
    nasa_apod_url = "https://api.nasa.gov/planetary/apod"
    count = 30
    params = {
        'api_key': nasa_token,
        'count': count
    }
    response = requests.get(nasa_apod_url, params=params)
    links = response.json()
    for link in links:
        if link.get('media_type') == 'image':
            if link.get('hdurl'):
                nasa_link = link['hdurl']
            else:
                nasa_link = link['url']
        extension, file_name = get_extension(nasa_link)
        path = os.path.join('images',f'{file_name}{extension}')
        download_images(path, nasa_link)


def main():
    nasa_token = os.environ['NASA_TOKEN']
    fetch_nasa_apod(nasa_token)


if __name__ == '__main__':
    main()
