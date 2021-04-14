#!/usr/bin/python3
from sender import *
from scanner import *


def main():
    # Define the constant emails and port
    port= 465
    smtp_email = "smtp.gmail.com"
    sender_email = "checkstockPT@gmail.com"
    Rpath = "receivers.csv"
    Wpath = "websites.csv"
    # Define the password and the receiver emails
    password = definer(Rpath)
    # Scan webpages and return gpu (not) available and correpondent website
    gpu, chip, site, store = scanner(Wpath)
    # Send the email
    sender(port, smtp_email, sender_email, Rpath, password, gpu, site)
    






if __name__ == '__main__':
    main()