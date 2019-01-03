#! /usr/bin/python
#
#	gmail_send.py
#
#					Jan/03/2019
# ------------------------------------------------------------------
import httplib2
import os
import sys

import apiclient
import oauth2client
import argparse
from oauth2client import file, client, tools
# ------------------------------------------------------------------
import base64
#from email.mime.text import MIMEText
from email.utils import formatdate
from email.message import EmailMessage
import traceback

SCOPES = "https://www.googleapis.com/auth/gmail.send"
CLIENT_SECRET_FILE = "credentials.json"
APPLICATION_NAME = "MyGmailSender"

# ------------------------------------------------------------------
# [6-4]:
def get_credentials(flags):
	script_dir =os.path.abspath(os.path.dirname(__file__)) 
	credential_dir = os.path.join(script_dir, ".credentials")

	if not os.path.exists(credential_dir):
		os.makedirs(credential_dir)
	credential_path = os.path.join(credential_dir,"my-gmail-sender.json")

	store = oauth2client.file.Storage(credential_path)
	credentials = store.get()
	if not credentials or credentials.invalid:
		flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
		flow.user_agent = APPLICATION_NAME
		credentials = oauth2client.tools.run_flow(flow, store, flags)
		print("Storing credentials to " + credential_path)
#
	return credentials
#
# ------------------------------------------------------------------
# [6-8]:
def create_message(mail_to,subject,str_message):
	message = EmailMessage()
	message.set_content(str_message)
#
	message["to"] = mail_to
	message["subject"] = subject
	message["Date"] = formatdate(localtime=True)

	byte_msg = message.as_string().encode(encoding="UTF-8")
	byte_msg_b64encoded = base64.urlsafe_b64encode(byte_msg)
	str_msg_b64encoded = byte_msg_b64encoded.decode(encoding="UTF-8")

	return {"raw": str_msg_b64encoded}
#
# ------------------------------------------------------------------
# [6]:
def gmail_send_proc(userId,mail_to,subject,str_message,flags):
	credentials = get_credentials(flags)
	http = credentials.authorize(httplib2.Http())
	service = apiclient.discovery.build("gmail", "v1", http=http)
#
	try:
		result = service.users().messages().send(
			userId=userId,
			body=create_message(mail_to,subject,str_message)
		).execute()

		print("Message Id: {}".format(result["id"]))

	except apiclient.errors.HttpError:
		print("------start trace------")
		traceback.print_exc()
		print("------end trace------")
#
# ------------------------------------------------------------------
