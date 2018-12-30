# ------------------------------------------------------------------
#
#	gmail_send/views.py
#
# ------------------------------------------------------------------
import sys
import os

from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from gmail_send.lib.gmail_send import gmail_send_proc 

# ------------------------------------------------------------------
def index(request):
	message = ""
	message += 'gmail_send からのメッセージです。<br />'
	message += str(request.user.id) + '&nbsp;&nbsp;'
	message += request.user.username + '<p />'
	dd = {
		'hour': datetime.now().hour,
		'minute': datetime.now().minute,
		'message': message,
	}
	return render(request, 'gmail_send/gmail_send.html', dd)
#
# ------------------------------------------------------------------
@csrf_exempt 
def gmail_main_proc(request):
	sys.stderr.write("*** gmail_main_proc *** start ***\n")
	print(request)
#
	if (request.method == 'POST'):
		flags = None
#
		userId = os.environ.get('userId')
		mail_to = request.POST['mail_to']
		subject = request.POST['subject']
		str_message = request.POST['str_message']
		str_message += "*** message ***\n"
		str_message += "userId: " + userId + "\n"
		str_message += "mail_to: " + mail_to + "\n"
		str_message += "*** message ***\n"
#
		sys.stderr.write("*** userId: " + userId + "\n")
		gmail_send_proc(userId,mail_to,subject,str_message,flags)
#
	sys.stderr.write("*** gmail_main_proc *** end ***\n")
	str_out = "Success"
	return HttpResponse(str_out)
# ------------------------------------------------------------------
