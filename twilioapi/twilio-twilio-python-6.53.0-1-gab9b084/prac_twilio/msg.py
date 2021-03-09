from twilio.rest import client

account_sid = "ACd160547821221161fe1b0ddb9f3eb443"
# Your Auth Token from twilio.com/console
auth_token = "your_auth_token"

client = client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309",
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
