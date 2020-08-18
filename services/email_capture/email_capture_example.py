import smtplib
import email.utils
from email.mime.text import MIMEText

SMTP_SERVER = 'capture.mailsac.com'
SMTP_PORT = 5587
SMTP_USERNAME = 'MAILSAC_USERNAME'
SMTP_PASSWORD = 'MAILSAC_API_KEY'
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
    conn.login(SMTP_USERNAME, SMTP_PASSWORD)
    conn.sendmail(FROM_ADDRESS, TO_ADDRESS, msg.as_string())
    conn.close()
except Exception as e:
    print('Error: ', e)
else:
    print('Email Sent')

"""
send: 'ehlo [127.0.1.1]\r\n'
reply: b'250-smtp-capture1-172-31-20-37 Welcome! [172.31.20.37:25]\r\n'
reply: b'250-SIZE 1048576\r\n'
reply: b'250-STARTTLS\r\n'
reply: b'250-AUTH PLAIN LOGIN\r\n'
reply: b'250-PROXY PROXY\r\n'
reply: b'250 HELP\r\n'
reply: retcode (250); Msg: b'smtp-capture1-172-31-20-37 Welcome! [172.31.20.37:25]\nSIZE 1048576\nSTARTTLS\nAUTH PLAIN LOGIN\nPROXY PROXY\nHELP'
send: 'STARTTLS\r\n'
reply: b'220 Ready to start TLS\r\n'
reply: retcode (220); Msg: b'Ready to start TLS'
send: 'ehlo [127.0.1.1]\r\n'
reply: b'250-smtp-capture1-172-31-20-37 Welcome! [172.31.20.37:25]\r\n'
reply: b'250-SIZE 1048576\r\n'
reply: b'250-AUTH LOGIN PLAIN\r\n'
reply: b'250-PROXY PROXY\r\n'
reply: b'250 HELP\r\n'
reply: retcode (250); Msg: b'smtp-capture1-172-31-20-37 Welcome! [172.31.20.37:25]\nSIZE 1048576\nAUTH LOGIN PLAIN\nPROXY PROXY\nHELP'
send: 'AUTH PLAIN AG1qbWF5ZXIAdzo4eXBTSkJqZUUxVlM5VkVLdDRueEUwSnNITE0=\r\n'
reply: b'235 Authentication succeeded\r\n'
reply: retcode (235); Msg: b'Authentication succeeded'
send: 'mail FROM:<no-reply@mywebapp.com> size=303\r\n'
reply: b'250 Accepted\r\n'
reply: retcode (250); Msg: b'Accepted'
send: 'rcpt TO:<mycustomer@gmail.com>\r\n'
reply: b'250 Accepted\r\n'
reply: retcode (250); Msg: b'Accepted'
send: 'data\r\n'
reply: b'354 Enter message, ending with "." on a line by itself\r\n'
reply: retcode (354); Msg: b'Enter message, ending with "." on a line by itself'
data: (354, b'Enter message, ending with "." on a line by itself')
send: b'Content-Type: text/plain; charset="us-ascii"\r\nMIME-Version: 1.0\r\nContent-Transfer-Encoding: 7bit\r\nSubject: Password reset\r\nFrom: Mywebapp Customer Support <no-reply@mywebapp.com>\r\nTo: mycustomer@gmail.com\r\n\r\nClick on the link to reset you password\r\nhttps://mywebapp.com/password-reset/PasswordResetToken\r\n.\r\n'
reply: b'250 OK : queued as cp8gFd4tZNmvAbvp_U4lgIhTOpgG\r\n'
reply: retcode (250); Msg: b'OK : queued as cp8gFd4tZNmvAbvp_U4lgIhTOpgG'
data: (250, b'OK : queued as cp8gFd4tZNmvAbvp_U4lgIhTOpgG')
Email Sent
"""
