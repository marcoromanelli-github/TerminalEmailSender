from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MessageManager:
    def __init__(self):
        self.SUBJECT = ""
        self.TEXT = ""
        self.message = ""
        self.FROM = ""
        self.TO = ""

    def initialize_message(self, sub, txt, from_, to):
        self.SUBJECT = sub
        self.TEXT = txt
        self.FROM = from_
        self.TO = to

    def compose_message(self):
        # self.message = 'Subject: {}\n\n{}'.format(self.SUBJECT, self.TEXT)

        msg = MIMEMultipart("alternative")
        msg["Subject"] = self.SUBJECT
        msg["From"] = self.FROM
        msg["To"] = self.TO
        msg.attach(MIMEText(self.TEXT, "plain"))

        self.message = msg.as_string()

        return self.message
