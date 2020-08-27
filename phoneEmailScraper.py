#! python3

import re, pyperclip

# Create regex obj for phone num
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\))) ?    #area code (optional)
(\s|-)                       #first separator
\d\d\d                       #first 3 digits
-                            #separator
\d\d\d\d                     #last 4 digits
(((ext(\.)?\s)|x)            #extension words (optinal)
(\d{2,5}))?
)                 #extension digits (optional)
''', re.VERBOSE)

#Create regex obj for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ #name part
@               #@ symbol
[a-zA-Z0-9_.+]+ #domain name
''', re.VERBOSE)

#Get text off clipboard
text = pyperclip.paste()

#\Extract email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#Copy extracted email/phone to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
