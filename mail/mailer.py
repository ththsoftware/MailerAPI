import smtplib
import socket


class Mailer:
    def __init__(self, message_from_name, message_from_email, message_subject, message_body):
        self.message_from_name = message_from_name.get('value')
        self.message_from_email = message_from_email.get('value')
        self.message_subject = message_subject.get('value')
        self.message_body = message_body.get('value')

    def send(self):
        port = 587
        smtp_server = "smtp.office365.com"
        smtp_address = socket.gethostbyname(smtp_server)
        login = "tomnt93@outlook.com"
        password = ""

        sender = "tomnt93@outlook.com"
        receiver = "thomas@ththsofware.com"
        message = f"""Subject: New message sent from ththsoftware.com\n\n
        Name: {self.message_from_name}
        Email: {self.message_from_email}
        Subject: {self.message_subject}

        {self.message_body}"""

        try:
            with smtplib.SMTP(smtp_address, port) as server:
                server.starttls()
                server.login(login, password)
                server.sendmail(sender, receiver, message)
            return "OK"
        except ():
            return "Backend failure, please try again.\
             If failure persists please go to the BugZapper project and create a ticket"



