#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import time
import csv

def scanner(path):
    while(1):
        with open(path) as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for name, chipset, website, store in reader:
                # Set the headers for a browser experience
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

                # Download webpage
                response = requests.get(website, headers=headers)
                # Saves all text
                soup = BeautifulSoup(response.text, "html.parser") 
                

                # If there is "Sem stock" in soup, it sleeps, if not, it breaks the loop and returns the GPU name and website
                if store == " PCDiga":
                    if str(soup).find("Sem stock") > 0:
                        time.sleep(1)
                        print('A GPU ' + name + ', na loja' + store + ', está sem stock!')
                        continue
                    else:
                        # If there is stock, check price and save it
                        pricehtml = soup.find_all('span', class_ = "price-wrapper")
                        pricelist = [item.text for item in pricehtml]
                        pricestr = ""
                        for ele in pricelist: 
                            pricestr += ele
                        print('A GPU ' + name + ' está em stock na loja' + store + ' e custa ' + pricestr + '!')
                        website = '"' + website + '"'
                        return name, chipset, website, store, pricestr
                        break
                elif store == " GlobalData":
                    if str(soup).find("Online - Esgotado") > 0:
                        time.sleep(1)
                        print('A GPU ' + name + ', na loja' + store + ', está sem stock!')
                        continue
                    else:
                        # If there is stock, check price and save it
                        pricehtml = soup.find_all('span', class_ = "price__amount")
                        pricelist = [item.text for item in pricehtml]
                        pricestr = ""
                        for ele in pricelist[0]: 
                            pricestr += ele
                        l = len(pricestr)
                        pricestr = pricestr[1:l-1]
                        print('A GPU ' + name + ' está em stock na loja' + store + ' e custa ' + pricestr + '!')
                        website = '"' + website + '"'
                        return name, chipset, website, store, pricestr
                        break
                    


