import smtplib
import email.utils
from email.mime.text import MIMEText

SMTP_SERVER = 'in.mailsac.com'
SMTP_PORT = 587
FROM_ADDRESS = 'no-reply@mywebapp.com'
FROM_NAME = 'Mywebapp Customer Support'
TO_ADDRESS = 'mycustomer@gmail.com'
SUBJECT = 'Password reset'
BODY_TEXT = ('Click on the link to reset you password\r\n'
             'https://mywebapp.com/password-reset/PasswordResetToken'
            )

msg = MIMEText(BODY_TEXT)
msg['Subject'] = SUBJECT
msg['From'] = email.utils.formataddr((FROM_NAME, FROM_ADDRESS))
msg['To'] = TO_ADDRESS

conn = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
conn.set_debuglevel(True)
conn.ehlo()
conn.starttls()
conn.ehlo()
try:
    conn.sendmail(FROM_ADDRESS, TO_ADDRESS, msg.as_string())
    conn.close()
except Exception as e:
    print('Error: ', e)
else:
    print('Email Sent')
