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
                            twiml='<Response><Say>Ahoy, World!</Say></Response>',
                            to=TO_NUMBER,
                            from_=FROM_Number
                        )

    print(call.sid)

if __name__ == "__main__":
    startpy()
