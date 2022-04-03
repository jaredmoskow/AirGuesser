import requests
from bs4 import BeautifulSoup


def getImages(site):
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all(class_='_6tbg2q')
    urls = [img['src'] for img in img_tags]
    return urls
