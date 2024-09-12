import os
import yagmail
from dotenv import load_dotenv

load_dotenv()

def send_email(to, subject, contents, attachments=None):
    """
    Send an email using yagmail, with sender credentials from environment variables.

    Parameters:
    -----------
    - to (str or list): The email address(es) of the recipient(s)
    - subject (str): The subject of the email
    - contents (str or list): The contents of the email
    - attachments (str or list, optional): Path(s) to file(s) to be attached

    Returns:
    --------
    - bool: True if the email was sent successfully, False otherwise
    """

    try:
        # Fetch sender's email and password from environment variables
        sender_email = os.getenv("EMAIL_USER")
        sender_password = os.getenv("EMAIL_PASS")

        # Initialize the Yagmail SMTP client with the sender's credentials
        yag = yagmail.SMTP(user=sender_email, password=sender_password)

        # Send the email
        yag.send(to=to, subject=subject, contents=contents, attachments=attachments)
        
        print("Email sent successfully!")
        return True

    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


# Example call to send an email
send_email(
    to='miladagdam@gmail.com',
    subject='Welcome to Our Service',
    contents='Hello, welcome to our service!',
    attachments=None
)
