from colorama import Fore, init
import requests
import random
import time
import os
from urllib.parse import urlparse
import hashlib
import string
import base64

# Initialisation de colorama
init(autoreset=True)

# Variable de couleur globale par défaut (Bleu)
color = Fore.BLUE

# Fonction pour afficher avec la couleur globale
def colored_print(text):
    global color
    print(color + text)

# Fonction d'affichage de la bannière avec la couleur dynamique
def print_banner():
    colored_print("""
                                        ██████  ▄▄▄       ██▀███    ▄████  ██▓
                                      ▒██    ▒ ▒████▄    ▓██ ▒ ██▒ ██▒ ▀█▒▓██▒
                                      ░ ▓██▄   ▒██  ▀█▄  ▓██ ░▄█ ▒▒██░▄▄▄░▒██▒
                                        ▒   ██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█  ██▓░██░
 [!] Settings                         ▒██████▒▒ ▓█   ▓██▒░██▓ ▒██▒░▒▓███▀▒░██░     [/] Discord Web
 [Q] Leave                           ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ░▒   ▒ ░▓  
                                     ░ ░▒  ░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░  ░   ░  ▒ ░
                                      ░  ░  ░    ░   ▒     ░░   ░ ░ ░   ░  ▒ ░
                                             ░        ░  ░   ░           ░  ░  
                                                                                           
╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                     ═══╗
║   [01] > Tool Info                 ║ ║ [05] > CheckYourIP                  ║ ║ [09] > Nitro Gen          ║
║   [02] > IP Lookup                 ║ ║ [06] > HashPassWord                 ║ ║ [10] > ID TO TOKEN        ║
║   [03] > Gen IP                    ║ ║ [07] > Clone Site [SCRAPPER]        ║ ║ [11] > Generator          ║
║   [04] > Gen Gmail                 ║ ║ [08] > Spam Webhook                 ║ ║ [12] > Dmall Friend             ║
╚═══                              ═══╝ ╚═══                               ═══╝ ╚═══                     ═══╝
""")

def display_tool_info():
    info = ("Multitool avec plusieurs fonctionnalités pour faciliter divers processus.")
    print(info)

def retrieve_my_ip():
    try:
        response = requests.get('https://api.ipify.org/')
        if response.status_code == 200:
            return (f"Votre adresse IP est : {response.text.strip()}")
    except:
        return ("Erreur lors de la récupération de votre adresse IP.")

def lookup_ip():
    ip_address = input("Entrer l'adresse IP : ")
    result = check_ip(ip_address)
    print(result)

def generate_random_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def check_ip(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        return (f"{ip_address} ✅") if response.status_code == 200 else (f"{ip_address} ❌")
    except Exception as e:
        return (f"Erreur lors de la vérification de l'IP: {str(e)}")

def generate_ips():
    num_ips = int(input("Combien d'adresses IP voulez-vous générer ? : "))
    for _ in range(num_ips):
        print(check_ip(generate_random_ip()))
        time.sleep(1)  

def generate_email():
    return f"user{random.randint(1000, 9999)}@{random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'])}"

def check_email(email_address):
    return (f"{email_address} ✅")

def gmail_generator():
    num_emails = int(input("Combien d'adresses Gmail voulez-vous générer ? : "))
    for _ in range(num_emails):
        print(check_email(generate_email()))
        time.sleep(1)

def hash_password():
    password = input("Entrer le mot de passe à hasher : ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print(f"Mot de passe hashé : {hashed_password}")

def clone_website():
    url = input("Entrer l'URL du site à cloner : ")
    site_name = urlparse(url).netloc.replace("www.", "")
    folder_name = site_name

    os.makedirs(folder_name, exist_ok=True)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(folder_name, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Le site {url} a été cloné dans le dossier '{folder_name}/index.html'.")
        else:
            print(f"Erreur lors de la récupération du site. Statut : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors du clonage : {str(e)}")

def send_webhook_spam():
    url = input("Entrez l'URL du webhook : ").strip()
    message = input("Message à envoyer : ").strip()
    num_messages = int(input("Nombre de fois à envoyer : ").strip())
    payload = {"content": message}

    print("Envoi des messages...")
    for _ in range(num_messages):
        response = requests.post(url, json=payload)
        if response.status_code == 204:
            print("Message envoyé.")
        else:
            print(f"Erreur d'envoi : Code {response.status_code}")
        time.sleep(1)

def generate_nitro_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def generate_nitro_codes():
    url = input("Entrez l'URL du webhook Discord : ").strip()
    num_codes = int(input("Nombre de codes Nitro à générer : ").strip())

    codes = [f"https://discord.gift/{generate_nitro_code()}" for _ in range(num_codes)]
    with open("valides_codes_nitro.txt", "w") as f:
        for code in codes:
            response = requests.post(url, json={"content": code})
            if response.status_code == 204:
                print(f"Code envoyé : {code}")
                f.write(code + "\n")
            else:
                print(f"Erreur d'envoi : {code} - Statut : {response.status_code}")
            time.sleep(1)

    print("Codes valides sauvegardés dans 'valides_codes_nitro.txt'.")

def id_to_token():
    userid = input("Entrer l'ID utilisateur : ")
    encoded = base64.b64encode(userid.encode("utf-8")).decode("utf-8")
    print(f'Token (première partie) : {encoded}')
    os.system('pause >nul')

def generate_gift_card():
    ascii_art = """
                    ███████████████████████████████████████████
                    █▌   +7 FEATURES GENERATOR !              █▌                              
                    █▌  ███████╗ █████╗ ██████╗  ██████╗ ██╗  █▌         ║══╗
                    █▌  ██╔════╝██╔══██╗██╔══██╗██╔════╝ ██║  █▌═════════╝  ║
                    █▌  ███████╗███████║██████╔╝██║  ███╗██║--||  GENERATOR █▌
                    █▌  ╚════██║██╔══██║██╔══██╗██║   ██║██║  █▌════════════╝
                    █▌  ███████║██║  ██║██║  ██║╚██████╔╝██║  █▌
                    █▌  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  █▌
                    ████████████████████████████████████████████
    """
    print(ascii_art)
    
    options = {
        '1': 'Amazon',
        '2': 'Netflix',
        '3': 'Roblox',
        '4': 'Apple',
        '5': 'Steam',
        '6': 'Google Play',
        '7': 'Spotify'
    }

    print("Options de cartes cadeaux disponibles :")
    for key, value in options.items():
        print(f"{key}: {value}")

    choice = input("Choisissez une option : ")
    if choice in options:
        num_codes = int(input("Combien de codes voulez-vous générer ? : "))
        for _ in range(num_codes):
            # Génère le code de la carte cadeau sans le vérifier
            code = f"{options[choice]} Code: {generate_nitro_code()}"  # Ou un autre format de code
            print(f"Code généré : {code}")
            time.sleep(3)  # Pause de 3 secondes entre chaque code
    else:
        print("Choix invalide.")

def dm_all_friends():
    token = input("Entrez votre token Discord : ")
    message = input("Entrez le message à envoyer : ")
    
    # URL de l'API Discord pour récupérer les amis
    url = "https://discord.com/api/v10/users/@me/relationships"
    headers = {
        "Authorization": token
    }

    try:
        response = requests.get(url, headers=headers)
        friends = response.json()

        if response.status_code == 200 and isinstance(friends, list):
            print(f"Nombre d'amis récupérés : {len(friends)}")
            for friend in friends:
                friend_id = friend["id"]
                send_dm_url = f"https://discord.com/api/v10/channels"
                dm_payload = {
                    "recipient_id": friend_id
                }
                
                # Création d'un DM channel avec l'ami
                channel_response = requests.post(send_dm_url, headers=headers, json=dm_payload)
                if channel_response.status_code == 201:
                    channel_id = channel_response.json()["id"]
                    message_payload = {
                        "content": message
                    }

                    # Envoi du message au DM channel
                    message_response = requests.post(f"https://discord.com/api/v10/channels/{channel_id}/messages", headers=headers, json=message_payload)
                    if message_response.status_code == 200:
                        print(f"Message envoyé à {friend_id} ✅")
                    else:
                        print(f"Erreur lors de l'envoi à {friend_id} : {message_response.status_code}")
                else:
                    print(f"Erreur lors de la création du DM avec {friend_id} : {channel_response.status_code}")
                
                time.sleep(1)  # Pour éviter d'être rate-limité
        else:
            print(f"Erreur lors de la récupération des amis : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de l'envoi des messages : {str(e)}")
def change_color():
    global color
    colored_print("Choisissez une couleur : ")
    print("1 - Rouge")
    print("2 - Bleu")
    print("3 - Jaune")
    print("4 - Violet")
    print("5 - Rose")
    print("6 - Vert")
    
    choice = input("Entrez le numéro de couleur : ").strip()
    if choice == '1':
        color = Fore.RED
    elif choice == '2':
        color = Fore.BLUE
    elif choice == '3':
        color = Fore.YELLOW
    elif choice == '4':
        color = Fore.MAGENTA
    elif choice == '5':
        color = Fore.LIGHTMAGENTA_EX
    elif choice == '6':
        color = Fore.GREEN
    else:
        colored_print("Choix invalide. La couleur par défaut sera appliquée.")

# Exemple d'une fonction qui utilise colored_print() au lieu de print
def display_tool_info():
    colored_print("Multitool avec plusieurs fonctionnalités pour faciliter divers processus.")

# Remplacer print par colored_print dans toutes les autres fonctions
def main_menu():
    while True:
        print_banner()
        choice = input(color + "Choisissez une option (1-11), '!' pour changer la couleur ou 'q' pour quitter : ").strip()
        if choice == '!':
            change_color()
        if choice == '01':
            display_tool_info()
        elif choice == '02':
            lookup_ip()
        elif choice == '03':
            generate_ips()
        elif choice == '04':
            gmail_generator()
        elif choice == '05':
            print(retrieve_my_ip())
        elif choice == '06':
            hash_password()
        elif choice == '07':
            clone_website()
        elif choice == '08':
            send_webhook_spam()
        elif choice == '09':
            generate_nitro_codes()
        elif choice == '10':
            id_to_token()
        elif choice == '11':
            generate_gift_card()
        elif choice == '12':
            dm_all_friends()
        elif choice.lower() == 'q':
            break
        else:
            print("Choix invalide, essayez à nouveau.")

if __name__ == "__main__":
     main_menu()
