"""
import requests

def sendgridmail(user):
	url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"
	payload = {
		"personalizations": [
			{
				"to": [{"email": user}],
				"subject": "Your Monthly expense is exceeded"
			}
		],
		"from": {"email": "vtnkvel@gmail.com"},
		"content": [
			{
				"type": "text/plain",
				"value": "Avoid spending money, your monthly expense is exceeded..."
			}
		]
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "8dbcdbb4e0msh2ca0fb8c6cfb3b9p13a154jsn1b29565d9fd5",
		"X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
	}
	response = requests.request("POST", url, json=payload, headers=headers)
	print(response.text)
	"""

from sendgrid import SendGridAPIClient 
import os
from sendgrid.helpers.mail import *
def sendgridmail(user):

	sg = SendGridAPIClient('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')
	from_email = Email("vtnkvel@gmail.com")
	to_email = To(user)
	subject = "EXPENSE TRACKER NOTIFICATION"
	content = Content("text/plain", "Your Expenses are exceeded your limits.Please be cautious")
	mail = Mail(from_email, to_email, subject, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	print(response.status_code)
	print(response.body)
	print(response.headers)