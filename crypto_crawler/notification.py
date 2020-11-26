# # we import the Twilio client from the dependency we just installed
# from twilio.rest import Client
# import smtplib
# import ssl
#
# from crypto_crawler.strategy import arbitrage_signal
#
#
# def send_email(msg):
#     port = 587  # For starttls
#     smtp_server = "smtp.gmail.com"
#     sender_email = "mikenyc1207@gmail.com"
#     receiver_email = "send@gmail.com"
#     password = ""
#
#     context = ssl.create_default_context()
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.ehlo()  # Can be omitted
#         server.starttls(context=context)
#         server.ehlo()  # Can be omitted
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, msg)
#
#
# def send_sms(msg):
#     # the following line needs your Twilio Account SID and Auth Token
#     client = Client("AC", "")
#
#     # change the "from_" number to your Twilio number and the "to" number
#     # to the phone number you signed up for Twilio with, or upgrade your
#     # account to send SMS to any phone number
#     client.messages.create(to="+13479560000",
#                            from_="+12064832138",
#                            body=msg)
#
#
# def alarm_arbitrage(prices):
#     """
#     send out email when there is arbitrage signal
#     :param prices: CryptoPrice
#     :return: bool
#     """
#     print(arbitrage_signal(prices))
#     # send_email(arbitrage_signal(prices))
