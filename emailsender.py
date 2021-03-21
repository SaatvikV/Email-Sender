#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:18:31 2021

@author: kunshsingh
"""

import smtplib, ssl, getpass

port = 465  # For SSL
username = input("Type your email address and press enter: ")
#kunshksingh@gmail.com
password = getpass.getpass(prompt = 'Type your password and press enter: ')
# Create a secure SSL context
context = ssl.create_default_context()
file = open("emails.txt","r")

sender_email = username #Replace with your own email address
receiver_email = file.readlines()
for i in range (0,len(receiver_email)):
    message = f"""\
To: {receiver_email[i]}
Subject: Group Interview Request (Template)

Good Morning,

We hope you are doing well during this time! Our names are Saatvik Vadlapatla and Kunsh Singh, and we're students from Chantilly High School. Though you are likely busy, we were hoping for the chance to personally interview you for 15 minutes to talk about and learn from your life experiences. We would love to talk for even longer if you'd like, but only as long as your time permits it.

Thank you for taking the time to read our email! Have a wonderful rest of your week.

Sincerely,
Kunsh Singh and Saatvik Vadlapatla
Chantilly High School
Chantilly, Virginia
Class of 2021
(***Delete*** >> This email was sent using python)
                                        """
    

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(username, password)
        server.sendmail(sender_email, receiver_email[i], message)
file.close()