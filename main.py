import smtp
import bot
import os
from colorama import Style, Fore, init

init()

def extract_code_blocks(content: str) -> str:
    """Extrait le contenu entre les délimiteurs ``` ```"""
    import re
    pattern = r'```(.*?)```'
    matches = re.findall(pattern, content, re.DOTALL)
    if not matches:
        return content
    matches = re.sub("^html", '', '\n'.join(matches))
    return matches

def loop(object: smtp.Smtp_send, Data, message_bot):
    for data in Data:
        print("Message reçu : " + data["content"])
        msg: str = bot.bot(message_bot, data["content"])
        msg = extract_code_blocks(msg)
        print("Message du bot : " + Fore.BLUE + msg + Fore.RESET)
        print(Fore.CYAN + "Envoie pour -> " + data["from"] + Fore.RESET)
        print("Mettez le sujet que vous répondez au mail pas défaut c'est Réponse")
        subject = input()
        if not subject:
            subject = "Réponse"
        print("Mettez le message que vous souhaitez répondre si la réponse du bot vous va pas ! laissez vide si vous souhaitez la réponse du bot")
        body = input()
        if not body:
            body = msg
        object.send_email(data["from"], subject, body)
    return

def main():
    file_path: str = "message_bot"
    if not os.path.isfile(file_path):
        os.system("echo '' >> message_bot")
    message_bot: str = open(file_path, encoding='utf8')
    message_bot = message_bot.read()
    if not message_bot:
        print(Fore.RED + "Vous devez écrire quelque chose dans le fichier message_bot" + Fore.RESET)
        return
    print(message_bot)
    init_smtp_and_imap = smtp.Smtp_send()
    
    data = init_smtp_and_imap.get_unread_emails()
    if not data:
        print("Aucun mail à afficher")
        return
    else:
        loop(init_smtp_and_imap, data, message_bot)

main()
