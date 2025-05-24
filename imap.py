import os
import imaplib
import email
from dotenv import load_dotenv

load_dotenv()

class Imap:
    def __init__(self):
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('APP_PASSWORD')
        self.imap_server = os.getenv('IMAP_SERVER') if os.getenv('IMAP_SERVER') else "imap.gmail.com"
        self.imap_port = os.getenv('IMAP_PORT') if os.getenv('IMAP_PORT') else 993
        self.connection = None

    def connect(self):
        if not self.password or not self.email:
            print("Vous devez mettre un email et un mot de passe d'application !")
            return False
        try:
            self.connection = imaplib.IMAP4_SSL(self.imap_server, int(self.imap_port))
            self.connection.login(self.email, self.password)
            return True
        except Exception as e:
            print(f"Erreur de connexion: {e}")
            return False

    def get_unread_emails(self):
        if not self.connection:
            if not self.connect():
                return []

        emails = []
        try:
            self.connection.select('INBOX', True)
            
            _, messages = self.connection.search(None, 'UNSEEN')
            
            
            for num in messages[0].split():
                _, msg = self.connection.fetch(num, '(RFC822)')
                email_body = msg[0][1]
                email_message = email.message_from_bytes(email_body)
                
                body = ""
                if email_message.is_multipart():
                    for part in email_message.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break
                        elif part.get_content_type() == "text/html":
                            body = part.get_payload(decode=True).decode()
                else:
                    body = email_message.get_payload(decode=True).decode()
                
                emails.append({
                    'subject': email_message['subject'],
                    'from': email_message['from'],
                    'date': email_message['date'],
                    'content': body
                })
                
            self.close()
                
            return emails
        except Exception as e:
            print(f"Erreur lors de la lecture des emails: {e}")
            self.close()
            return []
        
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection.logout()