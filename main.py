#!/usr/bin/python3
from sender import *


def main():
    # Define the constant emails and port
    port= 465
    smtp_email = "smtp.gmail.com"
    sender_email = "checkstockPT@gmail.com"
    path = "receivers.csv"
    #Define the password and the receiver emails
    password = definer(path)
    #Send the email
    sender(port, smtp_email, sender_email, path, password)
    






if __name__ == '__main__':
    main()