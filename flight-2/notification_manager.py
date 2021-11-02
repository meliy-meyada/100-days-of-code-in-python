import smtplib
from twilio.rest import Client

TWILIO_SID = "Your Twilio SID"
TWILIO_AUTH_TOKEN = "Your Twilio Auth Token"
TWILIO_VIRTUAL_NUMBER = "Your phone number Twilio"
TWILIO_VERIFIED_NUMBER = "Your phone number"
MAIL_PROVIDER_SMTP_ADDRESS =  "Your email setup smtp"
MY_EMAIL = "Your email"
MY_PASSWORD = "Your Password"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, "smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )