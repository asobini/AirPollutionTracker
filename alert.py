import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(index, from_email, from_password, to_email):
    if from_email is None or from_password is None or to_email is None:
        return

    # SMTP server details (for Gmail in this case)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Port for TLS

    # Create the MIME message (multipart message)
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Poor Air Quality Alert"
    msg.attach(MIMEText(f"The AQI has exceeded the threshold. Current AQI: {index}.", 'plain'))

    try:
        # Establish a connection to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(from_email, from_password)  # Log in to the email account
            text = msg.as_string()  # Convert the message to a string
            server.sendmail(from_email, to_email, text)  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

