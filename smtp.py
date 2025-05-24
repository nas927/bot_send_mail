import imap
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()
            
class Smtp_send(imap.Imap):
    def __init__(self):
        super().__init__()
        self.smtp_server = os.getenv('SMTP_SERVER') if os.getenv('SMTP_SERVER') else "smtp.gmail.com"
        self.smtp_port = os.getenv('SMTP_PORT') if os.getenv('SMTP_PORT') else 587
        self.smtp_connection = None
        self.name = os.getenv("NOM")

    def connect_smtp(self):
        try:
            self.smtp_connection = smtplib.SMTP(self.smtp_server, self.smtp_port)
            self.smtp_connection.starttls()
            self.smtp_connection.login(self.email, self.password)
            return True
        except Exception as e:
            print(f"Erreur de connexion SMTP: {e}")
            return False

    def send_email(self, to_email, subject, body):
        if not self.smtp_connection:
            if not self.connect_smtp():
                return False

        try:
            message = MIMEMultipart()
            if self.name:
                message['From'] = self.name + " <" + self.email + ">"
            else:
                message["From"] = self.email
            message['To'] = to_email
            message['Subject'] = subject

            message.attach(MIMEText(body, 'html'))

            self.smtp_connection.send_message(message)
            print("Message envoyé avec succès")
            
            return True
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email: {e}")
            return False
        
    def close_smtp(self):
        if self.smtp_connection:
            self.smtp_connection.quit()