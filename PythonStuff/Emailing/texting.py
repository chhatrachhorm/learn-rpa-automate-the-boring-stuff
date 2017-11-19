#! python3
# using www.twilio.com
# install twilio: pip install twilio

from twilio.rest import Client

print('Enter Twilio ASID: ', end='')
asid = input()
print('Enter Twilio AuthToken: ', end='')
token = input()
client = Client(asid, token)

# your registered phone number
myPhone = '+19418456962'
other = '+85586645395'
message = client.messages.create(
    body='Hello, you have won 152005$',
    from_=myPhone,
    to=other
)


