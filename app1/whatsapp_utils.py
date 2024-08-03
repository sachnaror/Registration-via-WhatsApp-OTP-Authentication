import os

from twilio.rest import Client


def send_otp_to_whatsapp(phone_number, otp):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')

    if not account_sid or not auth_token:
        raise ValueError("Twilio account SID or auth token is not set in environment variables.")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Your OTP code is: {otp}',
        from_='whatsapp:+14155238886',
        to=f'whatsapp:+{phone_number}'
    )
    print(f"Message sent: {message.sid}")
