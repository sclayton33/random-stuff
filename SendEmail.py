#! /usr/bin/python3.7

# Just a basic script to send a random image via email using SMTP.

import os
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendEmail(ImgFileName):
    image_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'your-email'
    msg['To'] = 'recipient-email'

    #Uncomment the below 2 lines to add text to message body
    #text = MIMEText("test")
    #msg.attach(text)
    image = MIMEImage(image_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()    #must be called again after starttls()
    s.login('your-email', 'your-password')
    s.sendmail('your-email', 'recipient-email', msg.as_string())
    s.quit()

path = 'path to images'
files = os.listdir(path)

#Uncomment below and enter name of this file if in same directory as images
#to prevent from being sent
#files.remove('SendEmail.py')

send = random.choice(files)

SendEmail(send)