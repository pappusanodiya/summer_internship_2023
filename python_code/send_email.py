import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'pspappu7354@gmail.com'
receiver_email = 'sanodiylucky@gmail.com'
subject = 'python generated mail'
message = 'I wanna to inform you that you account limit is over please reacharge now'

# Create a MIME message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'sanodiyalucky@gmail.com'
smtp_password = ''

# Create an SMTP session
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully.')
except smtplib.SMTPException as e:
    print('Error sending email:', str(e))