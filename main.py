import fade
import requests
import random
import time
import os
from urllib.parse import urlparse
import hashlib
import string
import base64

# Display banner
banner = fade.purpleblue(r"""
                                   ╔══════════════════════════════════════╗
                                   ║ ███████╗ █████╗ ██████╗  ██████╗ ██╗ ║       ├─────────────
                                   ║ ██╔════╝██╔══██╗██╔══██╗██╔════╝ ██║ ║       │ root@noodles
                                   ║ ███████╗███████║██████╔╝██║  ███╗██║ ║       │─────────────
                                   ║ ╚════██║██╔══██║██╔══██╗██║   ██║██║ ║       │ v : 0.02
"q" pour quitter                   ║ ███████║██║  ██║██║  ██║╚██████╔╝██║ ║       │─────────────
                                   ║ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ║
                                   ╚══════════════════════════════════════╝
                                                       
╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                     ═══╗
║   [01] > Info Outils              ║ ║ [05] > Mon IP                      ║ ║ [09] > Nitro Gen          ║
║   [02] > Recherche IP             ║ ║ [06] > Hash Mot de Passe           ║ ║ [10] > ID VERS TOKEN      ║
║   [03] > Gen IP                   ║ ║ [07] > Clone Site                  ║ ║  N/A                      ║
║   [04] > Gen Gmail                ║ ║ [08] > Spam Webhook                ║ ║  N/A                      ║
╚═══                              ═══╝ ╚═══                               ═══╝ ╚═══                     ═══╝
""")

def display_tool_info():
    info = fade.purpleblue("Multitool avec plusieurs fonctionnalités pour faciliter divers processus.")
    print(info)

def retrieve_my_ip():
    try:
        response = requests.get('https://api.ipify.org/')
        if response.status_code == 200:
            return fade.purpleblue(f"Votre adresse IP est : {response.text.strip()}")
    except:
        return fade.purpleblue("Erreur lors de la récupération de votre adresse IP.")

def lookup_ip():
    ip_address = input("Entrer l'adresse IP : ")
    result = check_ip(ip_address)
    print(result)

def generate_random_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def check_ip(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        return fade.purpleblue(f"{ip_address} ✅") if response.status_code == 200 else fade.purpleblue(f"{ip_address} ❌")
    except Exception as e:
        return fade.purpleblue(f"Erreur lors de la vérification de l'IP: {str(e)}")

def generate_ips():
    num_ips = int(input("Combien d'adresses IP voulez-vous générer ? : "))
    for _ in range(num_ips):
        print(check_ip(generate_random_ip()))
        time.sleep(1)  

def generate_email():
    return f"user{random.randint(1000, 9999)}@{random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'])}"

def check_email(email_address):
    return fade.purpleblue(f"{email_address} ✅")

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

# Main Menu
def main_menu():
    while True:
        print(banner)
        choice = input("Choisissez une option (1-10) ou 'q' pour quitter : ").strip()
        
        if choice == '1':
            display_tool_info()
        elif choice == '2':
            lookup_ip()
        elif choice == '3':
            generate_ips()
        elif choice == '4':
            gmail_generator()
        elif choice == '5':
            print(retrieve_my_ip())
        elif choice == '6':
            hash_password()
        elif choice == '7':
            clone_website()
        elif choice == '8':
            send_webhook_spam()
        elif choice == '9':
            generate_nitro_codes()
        elif choice == '10':
            id_to_token()
        elif choice.lower() == 'q':
            print("Merci d'avoir utilisé l'outil !")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main_menu()
