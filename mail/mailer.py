import smtplib


class Mailer:
    def __init__(self, message_from_name, message_from_email, message_subject, message_body):
        self.message_from_name = message_from_name
        self.message_from_email = message_from_email
        self.message_subject = message_subject
        self.message_body = message_body

    def send(self):
        port = 587
        smtp_server = "smtp.office365.com"
        login = "tomnt93@outlook.com"
        password = ""

        sender = "tomnt93@outlook.com"
        receiver = "thomas@ththsofware.com"
        message = f"""\
        Email: {self.message_from_email}
        Subject: {self.message_subject}
        From: {self.message_from_name}

        {self.message_body}"""

        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(login, password)
                server.sendmail(sender, receiver, message)
            return "OK"
        except ():
            return "Backend failure, please try again.\
             If failure persists please go to the BugZapper project and create a ticket"



