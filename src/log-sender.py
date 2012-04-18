'''
Created on Apr 18, 2012

@author: art3
'''

import os
import time
import smtplib

#defining the sending fuction
def sending(line):
    fromaddr = 'mail@mail.com'
    toaddrs  = 'mail@mail.com'
    msg = '''From: SellThruUs Webserver <webserver@pfteam4.com>
    To: SellThruUs Admin<admin@pfteam4.com>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: there is activity on the server
    
    <h1>This is the event:</h1>
    '''+line
    
    # Credentials (if needed)
    username = 'yourgmailusername'
    password = 'yourgmailpassword'
    
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    print("Your E-Mail has been sent!")
    server.quit()

f = open(r'/var/log/auth.log', 'r')

while True:
    lines = f.readlines()
    primelength=len(lines)
    print primelength
    for line in lines:
        print line
        sending(line)
        time.sleep(5)