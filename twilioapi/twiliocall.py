import os
from twilio.rest import Client
from decouple import config

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token  = config('TWILIO_AUTH_TOKEN')
FROM_Number = config('FROM_Number')
TO_NUMBER   = config('TO_NUMBER')

def startpy():

    client = Client(account_sid, auth_token)


    call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to=FROM_Number,
                            from_=TO_NUMBER
                        )

    print(call.sid)

if __name__ == "__main__":
    startpy()
