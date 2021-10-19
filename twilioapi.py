import os
from twilio.rest import Client
from decouple import config

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token  = config('TWILIO_AUTH_TOKEN')
FROM_Number = config('FROM_Number')
TO_NUMBER   = config('TO_NUMBER')
client      = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello there, We got surprise for you",
                     from_= FROM_Number,
                     to= TO_NUMBER
                 )

print(message.sid)