import smtplib, ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = input("Enter your email address: ")  # Enter your address
receiver_email = input("Enter your receiver address: ")   # Enter receiver address
password = getpass.getpass("Type your password and press enter: ")
# password = input("Type your password and press enter: ")

message = MIMEMultipart("alternative")
message["Subject"] = "Python sending email tests"
message["From"] = sender_email
message["To"] = receiver_email

html = """\
<html>
  <body>
    <p>Hello world</p>
  </body>
</html>
"""
# Turn these into html MIMEText objects
htmlCode = MIMEText(html, "html")

# Add HTML parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(htmlCode)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email, message.as_string())