from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "XXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+XXX", 
    from_="+XXX",
    body="It works?!")

print(message.sid)
