import twilio
from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = twilio.environ['TWILIO_ACCOUNT_SID']
auth_token = twilio.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages 
                .create(
                    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                    from_='+15017122661',
                    to='+918072380221'
                )

print(message.sid)
