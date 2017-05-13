import smtplib
from email.mime.text import MIMEText
from email.header import Header
jp = 'iso-2022-jp'
user = '****@**.**.jp'
passwd = '****'

smtp = smtplib.SMTP('mail.so-net.ne.jp', 587)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(user, passwd)

msg = MIMEText("このメールはPythonから送信".encode(jp), 'plain', jp)

msg['Subject'] = str(Header('こんにちは。Python', jp))
msg['From'] = user
msg['To'] = user

smtp.sendmail(user,
              [user],
              msg.as_string())
smtp.close()
