import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from jobpusher.drivers.base import BaseDriver
from jobpusher.utils import check_mail_fomat

class MailDriver(BaseDriver):
    def __init__(self, account: str, password: str, host: str, port: int = 465, use_ssl=True) -> None:
        """
        :param account: mail account
        :param password: mail password
        :param host: mail host
        :param port: mail port (default: 25)
        """
        self.account = account
        if not check_mail_fomat(account):
            raise Exception('Mail address format error')
        self.password = password
        self.host = host
        self.port = port
        self.use_ssl = use_ssl
        pass

    def auth(self) -> None:
        # auth mail host
        try:
            if self.use_ssl:
                smtp = smtplib.SMTP_SSL(self.host, self.port)
            else:
                smtp = smtplib.SMTP(self.host, self.port)
            self.smtp = smtp
        except smtplib.SMTPAuthenticationError:
            raise Exception('Authentication failed')
        
    def send(self, to: str, subject: str, content: str, attachments: list[str]) -> None:
        if not check_mail_fomat(to):
            raise Exception('Mail address format error')

        msg = MIMEMultipart()
        msg['From'] = formataddr(["JobPusher", self.account])
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        for attachment in attachments:
            if not os.path.exists(attachment):
                raise Exception(f'Attachment {attachment} not found')

            with open(attachment, 'rb') as f:
                part = MIMEApplication(f.read())
                part.add_header('Content-Disposition', 'attachment', filename=attachment)
                msg.attach(part)
        try:
            self.smtp.sendmail(self.account, to, msg.as_string())
        except smtplib.SMTPException:
            raise Exception('Send mail failed')