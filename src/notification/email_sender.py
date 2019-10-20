import smtplib
import ssl


def send_email(msg):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "mikenyc1207@gmail.com"
    receiver_email = "send@gmail.com"
    password = ""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
