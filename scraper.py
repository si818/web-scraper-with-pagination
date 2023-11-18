from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
count = 1

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='w-full rounded border')

    for i in items:
        itemName = i.find('h4').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s)  Price: %s, Item name: %s' % (count, itemPrice, itemName))
        count += 1

    next_page = soup.find('a', {'rel': 'next'})
    if next_page:
        url = urljoin(url, next_page['href'])
    else:
        break

