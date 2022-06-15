from inspect import Attribute
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import openpyxl


headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}

base_url = "https://www.amazon.com/s?k={}".format(suchbegriff).replace(' ', '+')

items = []
for i in range(1, int(seiten) + 1):
    print("Scrapen von Seite {}...".format(i))
    response = requests.get(base_url + "&page{}".format(i), headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    results = soup.find_all('div' , {'class': 's-result-item', 'data-component-type': 's-search-result'})

    for result in results:
        product_name = results.h2.text

        try:
            rating = result.find('i', {'class': 'a-icon'}).text
    
        except AttributeError:
            continue

        try:
            price1 = result.find('span', {'class': 'a-price-whole'}).text
            price2 = result.find('span', {'class': 'a-price-fraction'}).text
            price = float(price1 + price2)
            product_url = 'https://amazon.com' + result.h2.a['href']

            items.append([product_name, rating, price, product_url])
            
        except AttributeError:
            continue

    sleep(1.5)
    
df = pd.DataFrame(items, columns=['product', 'rating', 'price', 'product url'])
df.to_excel('{}.xlsx'.format(dateiname), index=False)