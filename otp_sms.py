# from twilio.rest import Client
import random
import string
# from config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE, AFRICASTALKING_API_KEY, AFRICASTALKING_USERNAME
# import africastalking

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

# def send_sms_otp(phone_number, otp):
#     client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
#     message = f"Your decryption OTP is: {otp}"
#     client.messages.create(to=phone_number, from_=TWILIO_PHONE, body=message)


# def send_sms_otp(phone_number: str) -> str:
#     service_sid = 'VAa4213003ee4d0bca3f44c002c21b28ed'

#     client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

#     verification = client.verify \
#         .v2 \
#         .services(service_sid) \
#         .verifications \
#         .create(to=phone_number, channel='sms')

#     print(f"Verification SID for {phone_number}: {verification.sid}")
#     return verification.sid

import requests
from config import BASE_URL, DEVICE_ID, API_KEY
# africastalking.initialize(AFRICASTALKING_USERNAME, AFRICASTALKING_API_KEY)
# sms = africastalking.SMS

def send_sms_otp(phone_number: str, otp: str):
    response = requests.post(
        f'{BASE_URL}/gateway/devices/{DEVICE_ID}/send-sms',
        json={
            'recipients': [phone_number],
            'message': otp
            },
         headers={'x-api-key': API_KEY}
            )       

    print(response.json())