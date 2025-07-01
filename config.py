# TWILIO_SID = "ACef375b12875f78c44dadb1da4a559352PN2d495f5fe36e84230c522b494797d0e1"
# TWILIO_AUTH_TOKEN = "5e900db2ed99845fbe8edfff1fe23fd4"
# TWILIO_PHONE = "+1 709 705 8527"


# TWILIO_SID = "ACef375b12875f78c44dadb1da4a559352PN2d495f5fe36e84230c522b494797d0e1"
# TWILIO_AUTH_TOKEN = "5e900db2ed99845fbe8edfff1fe23fd45e900db2ed99845fbe8edfff1fe23fd4"
# TWILIO_PHONE = "+1 709 705 8527"

# AFRICASTALKING_API_KEY = "5da0719d-11b0-475e-92c5-e85d7c878173"
# AFRICASTALKING_USERNAME = "Mac Abdallah"

import requests

BASE_URL = 'https://api.textbee.dev/api/v1'
API_KEY = '5da0719d-11b0-475e-92c5-e85d7c878173'
DEVICE_ID = '685bef15279700d071ee2181'

response = requests.post(
  f'{BASE_URL}/gateway/devices/{DEVICE_ID}/send-sms',
  json={
    'recipients': ['+1234567890'],
    'message': 'Hello from TextBee!'
  },
  headers={'x-api-key': API_KEY}
)

print(response.json())