
from django.conf import settings
from twilio.rest import Client


def send_whatsapp_message(to, message):
    account_sid = 'AC57ba5e608c6b3f1fd8f5ea1f9877614a'
    auth_token = '034988d8afcc9005e364ad031b46ccb1'
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_='+14155238886',
        to=f'whatsapp:{to}'
    )



