from inspect import Attribute
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import openpyxl



def webscraper():
    from GUI import seiten_dropdown, product_entry, dateiname_entry
    suchbegriff = product_entry.get()
    seiten = seiten_dropdown.get()
    global dateiname
    dateiname = dateiname_entry.get().replace(' ', '_')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept-Language': 'en-US, en;q=0.5'
    }

    base_url = 'https://www.amazon.de/s?k={}'.format(suchbegriff).replace(' ', '+')

    liste_name = []
    liste_preis = []


    for i in range(1, seiten + 1):
        print('Scrapen von Seite {}...'.format(base_url + '&page={0}'.format(i)))
        response = requests.get(base_url + '&page={}'.format(i), headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        for container in soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'}):
            try:
                product_name = container.find('span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'}).text
                liste_name.append(product_name)
            except AttributeError:
                continue    

            try:
                price = container.find('span', attrs={'class': 'a-price-whole'}).text
                liste_preis.append(price)
            except AttributeError:
                continue

        sleep(1.5)
        
    df = pd.DataFrame(zip(liste_name, liste_preis), columns=['Produktname', 'Preis in €'])
    df.to_excel('{}.xlsx'.format(dateiname), index=False)