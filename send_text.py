from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC1f5bab2c66d7929368d54fa6d031bebc"
auth_token = "990e78933f3ffc2587557a7a882f7428"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="This is a text from the internet",
	to="+16124238377", # Replace with your phone number
	from_="+16123459507") # Replace with your Twilio number
print message.sid
