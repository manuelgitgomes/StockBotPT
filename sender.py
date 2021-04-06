#!/usr/bin/python3
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import csv

port= 465
smtp_email = "smtp.gmail.com"
sender_email = "checkstockPT@gmail.com"
password = getpass.getpass(prompt = 'Type your password and press enter: ')
receiver_email = input('Type the emails to receive the alerts: ')


message = MIMEMultipart("alternative")
message["Subject"] = "Stock Disponível!"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Olá!
Somos a Check Stock PT e estamos a testar o envio de emails para detetar stocks.
Em breve irás receber atualizações de stock das tuas GPUs favoritas!
Até à próxima!"""
html = """\
<html>
  <body>
    <p>Olá!<br>
       Somos a Check Stock PT e estamos a testar o envio de emails para detetar stocks.<br>
       Em breve irás receber atualizações de stock das tuas GPUs favoritas!<br>
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
        sender_email, receiver_email, message.as_string()
    )
