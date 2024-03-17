import requests
from downloads_images import downloads_images

def fetch_spacex_last_launch():
  url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
  response = requests.get(url)
  links = response.json()['links']['flickr']['original']
  for number_link, link in enumerate(links):
      file_name = f'images/spacex{number_link}.jpg'
      downloads_images(file_name, link)


def main():
    fetch_spacex_last_launch()

if __name__ == '__main__':
    main()