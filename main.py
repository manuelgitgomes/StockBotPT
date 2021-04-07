#!/usr/bin/python3
from sender import *


def main():
    # Defines the constant emails and port
    port= 465
    smtp_email = "smtp.gmail.com"
    sender_email = "checkstockPT@gmail.com"
    #Defines the password and the receiver email
    password, receiver_email = definer()
    #Sends the email
    sender(port, smtp_email, sender_email, receiver_email, password)





if __name__ == '__main__':
    main()