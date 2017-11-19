#! python3
# sending mail with smtp protocol
import getpass
import smtplib

smtp = smtplib.SMTP('smtp.gmail.com', 587)
# start tls
smtp.starttls()

print('Email: ', end='')
email, password = input(), getpass.getpass()

smtp.login(email, password)
smtp.sendmail(
    email,
    'ch.chhatra@gmail.com',
    'Subject: Silly Thing'
)

smtp.quit()
