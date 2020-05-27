from twilio.rest import Client

account_sid = '****account_sid****'
auth_token = '***auth_token***'
client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='+15868002066',
    body='This is a Python Generated SMS!',
    to='your_phone_number'
)
print(message.sid)
