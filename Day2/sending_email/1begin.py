import os
import smtplib                              #inbuilt

email_add = 'prazwolstark@gmail.com'                              #senders email
passwd_pass  = input("Enter the password of the account:  ") 
#app generated password
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login( email_add , passwd_pass)

    subject = 'Hi!'
    body = 'Howdy!'

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(email_add , '077bct055.prajjwal@pcampus.edu.np', msg)     #receivers email
