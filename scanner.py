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
                soup = BeautifulSoup(response.text, "lxml")

                # If there is "Sem stock" in soup, it sleeps, if not, it breaks the loop and returns the GPU name and website
                if str(soup).find("Sem stock") > 0:
                    time.sleep(1)
                    print('A GPU ' + name + ' está sem stock!')
                    continue
                else:
                    print('A GPU ' + name + ' está em stock!')
                    website = '"' + website + '"'
                    return name, chipset, website, store
                    break
                    


