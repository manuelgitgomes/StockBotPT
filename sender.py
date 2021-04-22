#!/usr/bin/python3
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import csv
import os

def definer(path):
  # Define the password
  password = getpass.getpass(prompt = 'Type your password and press enter: ')
  # Define the name, email, chipset and maximum price of a new receiver, write that information on a csv file
  with open(path, '+a') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    name = 'name'  
    while (1):
          name = input("Type the name of one of the new receivers: ")
          if (not name):
            break
          email = input("And the corresponding email: ")
          if (not email):
            break
          chipset = input("The desired chipset: ")
          if (not name):
            break
          price = input("And the maximum price: ")
          if (not email):
            break
          w.writerow([name, email, chipset, price])

  return password




def sender(port, smtp_email, sender_email, path, password, gpu, site, pricestr, priceint):
  # Read the csv file and sends the email for each receiver
  with open(path) as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for name, email, des_chipset, des_price in reader:
        # Converts desired price into integer
        des_priceint = int(des_price)
        # If the price is lower than the receiver is willing to pay, send email
        if priceint <= des_priceint:
          # Create the message subject, from and to
          message = MIMEMultipart("alternative")
          message["Subject"] = "Stock Disponível!"
          message["From"] = sender_email
          message["To"] = email

          # Create the plain-text and HTML version of your message
          text = """\
          Olá, """ + name + """!
          Somos a Check Stock PT e estamos a testar o envio de emails para detetar stocks.
          A GPU """ + gpu + """ está em stock aqui, e custa """ + pricestr + """.
          Até à próxima!"""
          html = """\
          <html>
          <body>
            <p>Olá, """ + name + """!<br>
              Somos a Check Stock PT e estamos a testar o envio de emails para detetar stocks.<br>
              A GPU """ + gpu + """ está em stock 
              <a href=""" + site + """>aqui</a>, e custa """ + pricestr + """. <br>
              Até à próxima!
            </p>
          </body>
          </html>
          """

          # Turn these into plain/html MIMEText objects
          part1 = MIMEText(text, "plain")
          part2 = MIMEText(html, "html")

          # Add HTML/plain-text parts to MIMEMultipart message
          # The email client will try to render the last part first
          message.attach(part1)
          message.attach(part2)

          # Create secure connection with server and send email
          context = ssl.create_default_context()
          with smtplib.SMTP_SSL(smtp_email, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, email, message.as_string()
            )
          print("Sending email to " + name)

          # Notify the email is being sent
          notify()
        else:
          # When the price is higher than desirable
          print("Email not sent to " + name + " because the price of the GPU (" + pricestr + ") is higher than the desired price (" + des_price + ")")


          


def notify():
  # Play a sound notification to alarm the user that email has been sent
  duration = 1  # seconds
  freq = 440  # Hz
  os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


