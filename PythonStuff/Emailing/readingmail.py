#! python3
# retrieving and deleting email with IMAP protocol
# builtin is imaplib
# to install imapclient => pip install imapclient==0.13

import imapclient
import getpass
import pprint

imap = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print('Email: ', end='')
email = input()
imap.login(email, getpass.getpass())

# navigate to inbox
pprint.pprint(imap.list_folders())
imap.select_folder('INBOX', readonly=False)
UIDs = imap.search(['SINCE 01-MAY-2015'])
print(UIDs)

# fetch email and make it as read
rawMessages = imap.fetch(7, ['BODY[]'])
pprint.pprint(rawMessages)


# delete email
imap.delete_messages(11)

# logout
imap.logout()
