from twilio.rest import Client

TWILIO_SID = "ACcf18d856cb0b6c48ddc4d335e8c78cea"
TWILIO_AUTH_TOKEN = "9e5210f66df8ca292fb1fe670c34008c"
TWILIO_VIRTUAL_NUMBER = "+16073006224"
TWILIO_VERIFIED_NUMBER = "+84987941901"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)