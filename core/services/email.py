from dataclasses import dataclass
from django.core.mail import send_mail
from django.template.loader import get_template
from typing import List
import smtplib
import datetime

@dataclass
class Email:
    subject: str
    message: str
    recipient_list: List[str]

    def get_date(self):
        today = datetime.date.today()
        formatted_date = today.strftime("%A %d %B, %Y")
        return formatted_date


    def generate_html(self):
        return get_template('email.html').render({
            'message': self.message,
            'subject': self.subject,
            'date': self.get_date(),
        })
    
    def send(self) -> None:
        message_html = self.generate_html()

        for recipient_email in self.recipient_list:            
            try:
                send_mail(
                    subject=self.subject,
                    html_message=message_html,
                    message='',
                    from_email='ZaCh Events and Catering',
                    recipient_list=[recipient_email],
                    fail_silently=False,
                )
            except smtplib.SMTPRecipientsRefused as error:
                print(error)
                pass