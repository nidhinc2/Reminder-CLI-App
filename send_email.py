#import schedule

import smtplib, ssl
import getpass
from email.message import EmailMessage

def send_email():
    port = 465

    sender_email = input("Sender Email : ")
    sender_password = getpass.getpass(prompt = "Sender email Password : ")
    #sender_password = input("Sender email Password : ")
    receiver_email = input("Receiver Email : ")

    # Create the email content
    mail = EmailMessage()
    mail["From"] = sender_email
    mail["To"] = receiver_email
    mail["Subject"] = "Test Email"
    mail.set_content(" Hi Nidhi, just testing if my code works!!  ")
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(send_emailer, sender_password)
        server.sendmail(sender_email, receiver_email, mail.as_string())
send_email()        
