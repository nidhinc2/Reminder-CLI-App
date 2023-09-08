import schedule
import time
import smtplib, ssl
import getpass
from email.message import EmailMessage

def send_email():
    port = 465

    sender_email = input("Sender Email : ")
    sender_password = getpass.getpass(prompt = "Sender email Password : ")
    #sender_password = input("Sender email Password : ")
    receiver_email = input("Receiver Email : ")
    mail_subject = input("Set the subject of your email")
    mail_content = input("Send the content of your email")

    # Create the email content
    mail = EmailMessage()
    mail["From"] = sender_email
    mail["To"] = receiver_email
    mail["Subject"] = mail_subject
    mail.set_content(mail_content)
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(send_emailer, sender_password)
        server.sendmail(sender_email, receiver_email, mail.as_string())


time_w = input("What time do you want to schedule it: ") 
schedule.every().day.at(time_w).do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)    
