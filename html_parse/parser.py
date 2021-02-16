from bs4 import BeautifulSoup
import requests

def parser_function(url):
    if 'defacto.com.tr' in url:
        response = requests.get(url=url)
        soup = BeautifulSoup(response.content,'lxml')
        price = soup.find('div',attrs={'class': "product-info-prices-new"}).text
        a_tag = soup.find('a', attrs={"class": "product-images-carousel-link"})
        image = a_tag.find('img')['src']
        return image, price
    image = None
    price = None
    return image, price
