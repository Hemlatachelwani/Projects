


# before sending email you have to enable your 2-step authentication and use app password instead of ur gmail password with your sending mail (xyz@gmail.com)

import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "chk935595@gmail.com"                         # your email-id goes here
EMAIL_PASSWORD = "fkikbsgxuhfojufz"                                  # your password goes here

msg = EmailMessage()
msg['Subject'] = 'this is subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

msg.set_content('Content area')

msg.add_alternative("""\
<html>
<body>
    <h1>Your HTML CONTENT GOES HERE Yaaaaaa!!!! </h1>                                
</body>
</html>
""", subtype='html')

with open('testing.txt', 'rb') as f:                       # your filename will go here
    file_data = f.read()
    file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    print("Login done!")
    smtp.send_message(msg)
    print("Email Sent Successfully ..")
