import requests
import argparse
from download_image import download_image


def fetch_spacex_last_launch(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    links = response.json()['links']['flickr']['original']
    for number_link, link in enumerate(links):
        file_name = f'images/spacex{number_link}.jpg'
        download_image(file_name, link)


def main():
    parser = argparse.ArgumentParser(
      description='Эта программа позволит вам скачать фотографии с запуска SpaceX.'
    )
    parser.add_argument(
      '--id',
      dest='launch_id',
      default='5eb87d47ffd86e000604b38a',
      help='Укажите ID запуска SpaceX, с которого можно загрузить фотографии.'
    )
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)
  

if __name__ == '__main__':
    main()
