# Introduction

Cette outil sert à ouvrir vos mail via imap protocol lire tous les mail et répondre à ces mail à l'aide d'un bot vous devez mettre un contexte par exemple vous êtes une entreprise de textile situé mettez le plus de chose possible pour que votre bot sera le plus précis possible

# Comment ça marche

A chaque message reçu le il sera marqué comme lu sur gmail

A chaque message le bot va générer une réponse
Vous allez voir la réponse en bleu dans la console

Vous pourrez changer le sujet et entrant un sujet sinon laisser vide par défaut c'est Réponse 
Vous pourrez changer le message généré s'il ne vous plaît pas sinon laissez vide

une fois validé votre mail va s'envoyer et ainsi de suite à chaque message

# chose à faire

version de python utilisé 3.12.6

git clone https://github.com/nas927/bot_send_mail.git
cd bot_send_mail
pip install -r requirements.txt
python main.py
