import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def createEmail(selectedEmail):
    port = 465  # For SSL
    password = "kPiCzcZJzd5sx8p"

    sender_email = "applockernoreply@gmail.com"
    receiver_email = selectedEmail

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hey,
    Someone is trying to log into one of your Programs.
    Maybe check your Computer.
    """

    html = """\
    <html>
      <body>
        <p Hey,<br>
           Someone is trying to log into one of your Programs.<br>
           Maybe check your Computer.<br>
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent")


