#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import time
import csv
import cloudscraper
import pandas as pd

def scanner(path, c):
    while(1):
        # Opening csv
        with open(path) as file:
            reader = csv.reader(file)

            # Count the number of lines on the csv
            lines = len(pd.read_csv(path)) 

            # Skip the already checked lines
            for x in range(0, c):
                next(reader)  
                
            for name, chipset, website, store in reader:
                # For each line scanned, add a count to c. If the count is larger than the number of lines, reset it.
                if c < lines:
                    c = c+1
                else:
                    c = 0

                # If the store is PCDiga
                if store == " PCDiga":
                    # Set the headers for a browser experience
                    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                    # Download webpage
                    response = requests.get(website, headers=headers)
                    # Saves all text
                    soup = BeautifulSoup(response.text, "html.parser") 

                    # If there is "Sem stock" in soup, it sleeps, if not, it breaks the loop and returns the GPU name and website
                    if str(soup).find("Sem stock") > 0:
                        time.sleep(0.01)
                        print('The GPU ' + name + ' is out of stock on' + store)
                        continue
                    else:
                        # If there is stock, check price and save it
                        pricehtml = soup.find_all('span', class_ = "price-wrapper")
                        pricelist = [item.text for item in pricehtml]
                        pricestr = ""
                        for ele in pricelist: 
                            pricestr += ele
                        print('The GPU ' + name + ' is in stock on' + store + ', costing ' + pricestr + '!')
                        website = '"' + website + '"'

                        # Transforms the string into an integer
                        pricestr2 = pricestr.replace(u'\xa0', u'')
                        priceint = int(pricestr2[:(len(pricestr2)-4)])

                        return name, chipset, website, store, pricestr, priceint, c
                        break

                # If the store is GlobalData
                elif store == " GlobalData":
                    # Due to GlobalData anti-DDoS software, another way to get text was needed
                    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
                    soup2 = scraper.get(website).text


                    # If there is "Online - Esgotado" in soup2, it sleeps, if not, it breaks the loop and returns the GPU name and websit
                    if str(soup2).find("Online - Esgotado") > 0:
                        time.sleep(0.01)
                        print('The GPU ' + name + ' is out of stock on' + store)
                        continue
                    else:
                        # If there is stock, check price and save it
                        priceclass = '<span class="price__amount">'
                        priceplc = soup2.find(priceclass)
                        l = len(priceclass)
                        pricestr = soup2[priceplc+l:]
                        europlc = pricestr.find('€')
                        pricestr = pricestr[:europlc+1]
                        pricestr = pricestr.replace(u'\n',u'')
                        print('The GPU ' + name + ' is in stock on' + store + ', costing ' + pricestr + '!')
                        website = '"' + website + '"'
                        
                        # Transforms the string into an integer
                        pricestr2 = pricestr.replace(u'\xa0', u'')
                        priceint = int(pricestr2[:(len(pricestr2)-4)])

                        return name, chipset, website, store, pricestr, priceint, c
                        break

                # If the store is GlobalData
                elif store == " CHIP7":
                    # Set the headers for a browser experience
                    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                    # Download webpage
                    response = requests.get(website, headers=headers)
                    # Saves all text
                    soup = BeautifulSoup(response.text, "html.parser") 

                    # If there is "Esgotado" in soup, it sleeps, if not, it breaks the loop and returns the GPU name and website
                    if str(soup).find("Esgotado") > 0:
                        time.sleep(0.01)
                        print('The GPU ' + name + ' is out of stock on' + store)
                        continue
                    else:
                        # If there is stock, check price and save it
                        pricehtml = soup.find_all('span', class_ = "price")
                        pricelist = [item.text for item in pricehtml]
                        pricestr = ""
                        for ele in pricelist[2]: 
                            pricestr += ele
                        print('The GPU ' + name + ' is in stock on' + store + ', costing ' + pricestr + '!')
                        website = '"' + website + '"'

                        # Transforms the string into an integer
                        priceint = int(price[:(len(price)-5)])
                        return name, chipset, website, store, pricestr, priceint, c
                        break
                    


