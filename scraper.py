import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='w-full rounded border')
count = 1

for i in items:
    itemName = i.find('h4').text.strip('\n')
    itemPrice = i.find('h5').text
    print('%s)  Price: %s, Item name: %s' % (count, itemPrice, itemName))
    count = count + 1

pages = soup.find('nav', class_='pagination')
urls = []
links = pages.find_all('a', class_='page')

for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)

print(urls)

for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='w-full rounded border')

