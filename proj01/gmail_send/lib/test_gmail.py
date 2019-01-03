#! /usr/bin/python
#
#	test_gmail.py
#
#					Dec/30/2018
# ------------------------------------------------------------------
import sys
import os

import environ
import argparse
import oauth2client

from gmail_send import gmail_send_proc 

flags = argparse.ArgumentParser(
    parents=[oauth2client.tools.argparser]
).parse_args()

# ------------------------------------------------------------------
sys.stderr.write("*** 開始 ***\n")
#
env = environ.Env(DEBUG=(bool, False),) # set default values and casting
environ.Env.read_env('.env') # reading .env file
#
userId = env('userId')
mail_to = "ccc@example.com"
#
subject = "Gmail Api Test Jan/03/2018 PM 17:11"
str_message = ""
str_message += "おはよう\n"
str_message += "晴れています。\n"
str_message += "Jan/03/2018 PM 17:11\n"
#
print(flags)
#
sys.stderr.write("userId: " + userId + "\n")
sys.stderr.write("mail_to: " + mail_to + "\n")
sys.stderr.write("subject: " + subject + "\n")
#
gmail_send_proc(userId,mail_to,subject,str_message,flags)
#
sys.stderr.write("*** 終了 ***\n")
# ------------------------------------------------------------------
