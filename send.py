import os
import smtplib
import ssl


def send_email(message):
    username = 'sprakash222.sp@gmail.com'
    password = os.getenv("PASSWORD")

    host = 'smtp.gmail.com'
    port = 465

    receiver = 'sprakash222.sp@gmail.com'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user=username, password=password)
        server.sendmail(username, receiver, message)



