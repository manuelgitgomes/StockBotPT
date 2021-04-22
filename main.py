#!/usr/bin/python3
from sender import *
from scanner import *


def main():
    # Define the constant emails, port, paths and a counter
    port= 465
    smtp_email = "smtp.gmail.com"
    sender_email = "checkstockPT@gmail.com"
    Rpath = "receivers.csv"
    Wpath = "websites.csv"
    c = 0
    # Define the password and the receiver emails
    password = definer(Rpath)

    # After an email is sent, continue scanning
    while (1):
        # Scan webpages and return gpu available and correpondent website
        gpu, chip, site, store, pricestr, priceint, c = scanner(Wpath, c)
        # Send the email
        sender(port, smtp_email, sender_email, Rpath, password, gpu, site, pricestr, priceint)






if __name__ == '__main__':
    main()