'''
import re
try:
    str=input('enter your pan number ?')
    obj=re.search(r'([A-Z]{5}[0-9]{4}[A-Z])',str)
    print (obj.group())
except:
    print ('pan number is not valid')

import time

sec=time.time()
print (sec)

curr=time.localtime(sec)
print (curr)

asi=time.asctime()
print (asi)

print (time.strftime("%d %M %y",curr))

'''

import smtplib
sender = 'vidyadharkongara@gmail.com'
receivers = ['vidyakongara90@gmail.com']
message = """From: From Person <mskanth29@gmail.com>
To: To Saikrishna<'sr1hfm@gmail.com'>
Subject: SMTP e-mail test
Hi All,
This is the first mail through python.
"""
print("THARUN")
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('vidyadharkongara@gmail.com','9963535610')
smtpObj.sendmail(sender, receivers, message)
print('mail sent from vidyadharkongara@gmail.com')
