#Scanning QR code
from email import message
import pyzbar.pyzbar as pyzbar
import cv2
import numpy

#Date and Time
import datetime 
import pytz
current_time = datetime.datetime.now (pytz.timezone('Asia/Manila'))

# Sending Message from QR code to email
from email import message
from http import server
import smtplib
sender_email = input ("Please type your email address: ")
password = input ("Password: ")
reciever_email = input ("Please type the reciever's email address: ")
server = smtplib.SMTP ("smtp.gmail.com" , 587)
server.ehlo ()
server.starttls ()
server.login (sender_email,password)

#Scanning QR Code
def scan ():
    i = 0
    cap  = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while i <1:
        _, frame = cap.read ()
        decoded =  pyzbar.decode (frame)
        for obj in decoded:
            qr_code_data = (obj.data)
            print (f"{qr_code_data}\n{current_time}")
            i = i+1
        cv2.imshow ("QRCode", frame)
        cv2.waitKey (5)
        cv2.destroyAllWindows 
    return qr_code_data
qr_code_data = scan ()

def email (qr_code_data):
    server.sendmail("airaestur@gmail.com", reciever_email , f"Subject:Message from the QR Code\n\n {qr_code_data}\n{current_time}")
    print (f"The messsage has been sent to: {reciever_email}, please check your email")
server.quit 
email(qr_code_data)

