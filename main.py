import fade
import requests
import random
import time
import os
from urllib.parse import urlparse
import hashlib
import string
import base64

themain = fade.purpleblue(r"""
                                   ╔══════════════════════════════════════╗
                                   ║ ███████╗ █████╗ ██████╗  ██████╗ ██╗ ║       ├─────────────
                                   ║ ██╔════╝██╔══██╗██╔══██╗██╔════╝ ██║ ║       │ root@noodles
                                   ║ ███████╗███████║██████╔╝██║  ███╗██║ ║       │─────────────
                                   ║ ╚════██║██╔══██║██╔══██╗██║   ██║██║ ║       │ v : 0.02
"q" quit the tool                  ║ ███████║██║  ██║██║  ██║╚██████╔╝██║ ║       │─────────────
                                   ║ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ║
                                   ╚══════════════════════════════════════╝
                  Débute l'osint des maintenant avec SARGI tool !
╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                     ═══╗
║   [01] > Tools Info                ║ ║ [05] > Your Ip                      ║ ║ [09] > Nitro Gen          ║
║   [02] > Ip Lookup                 ║ ║ [06] > PassWord Hashing             ║ ║ [10] > ID TO TOKEN        ║
║   [03] > IP Gen                    ║ ║ [07] > SiteCloner                   ║ ║  N/A                      ║
║   [04] > GMail Gen                 ║ ║ [08] > Webhook Spammer              ║ ║  N/A                      ║
╚═══                              ═══╝ ╚═══                               ═══╝ ╚═══                     ═══╝
""")

def toolinfo():
    info = fade.purpleblue("Ceci est un multitool qui inclut plusieurs fonctionnalités.\nDéveloppé pour faciliter des choses..")
    print(info)

def get_my_ip():
    response = requests.get('https://api.ipify.org/')
    if response.status_code == 200:
        my_ip = response.text.strip()
        return fade.purpleblue(f"Votre adresse IP est : {my_ip}")
    else:
        return fade.purpleblue("Erreur lors de la récupération de votre adresse IP.")

def ip_lookup():
    ip_address = input("Veuillez entrer l'adresse IP à rechercher : ")
    result = check_ip(ip_address)
    print(result)

def generate_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def check_ip(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        if response.status_code == 200:
            result = fade.purpleblue(f"{ip_address} ✅")
        else:
            result = fade.purpleblue(f"{ip_address} ❌")
        return result
    except Exception as e:
        return fade.purpleblue(f"Erreur lors de la vérification de l'IP: {str(e)}")

def ip_generator():
    num_ips = int(input("Combien d'adresses IP voulez-vous générer ? : "))
    for _ in range(num_ips):
        ip_address = generate_ip()
        result = check_ip(ip_address)
        print(result)
        time.sleep(1)  

def generate_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    return f"user{random.randint(1000, 9999)}@{random.choice(domains)}"

def check_email(email_address):
    result = fade.purpleblue(f"{email_address} ✅")
    return result

def gmail_generator():
    num_emails = int(input("Combien d'adresses Gmail voulez-vous générer ? : "))
    for _ in range(num_emails):
        email_address = generate_email()
        result = check_email(email_address)
        print(result)
        time.sleep(1) 

def password_hashing():
    password = input("Veuillez entrer le mot de passe à hasher : ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print(f"Le mot de passe hashé est : {hashed_password}")

def site_cloner():
    url = input("Veuillez entrer l'URL du site à cloner : ")
    parsed_url = urlparse(url)
    site_name = parsed_url.netloc.replace("www.", "")  
    folder_name = site_name

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(folder_name, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Le site {url} a été cloné  dans le dossier '{folder_name}/index.html'.")
        else:
            print(f"Erreur lors de la récupération du site. Statut : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors du clonage du site : {str(e)}")

def webhook_spammer():
    url = input("Entrez l'URL du webhook Discord : ").strip()
    message = input("Entrez le message que vous souhaitez envoyer : ").strip()
    num_messages = int(input("Entrez le nombre de fois que le message doit être envoyé : ").strip())

    payload = {"content": message}

    print("Envoi des messages...")
    for _ in range(num_messages):
        response = requests.post(url, json=payload)
        if response.status_code == 204:
            print("Message envoyé avec succès.")
        else:
            print(f"Erreur d'envoi du message : Code {response.status_code}")
        time.sleep(1)  # Ajouter une pause pour éviter d'envoyer les messages trop rapidement

def generate_nitro_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def nitro_generator():
    url = input("Entrez l'URL du webhook Discord : ").strip()
    num_codes = int(input("Entrez le nombre de codes Nitro à générer : ").strip())

    codes = [generate_nitro_code() for _ in range(num_codes)]
    valid_codes = []

    for code in codes:
        full_code = f"https://discord.gift/{code}"
        payload = {"content": full_code}

        # Envoi du code Nitro au webhook
        response = requests.post(url, json=payload)
        if response.status_code == 204:
            print(f"Code envoyé : {full_code}")
            valid_codes.append(full_code)
        else:
            print(f"Erreur lors de l'envoi du code : {full_code} - Statut : {response.status_code}")
        time.sleep(1)  # Pause pour éviter le spam

    # Enregistrement des codes valides dans un fichier
    with open("valides_codes_nitro.txt", "w") as f:
        for code in valid_codes:
            f.write(code + "\n")

    print(f"{len(valid_codes)} codes valides ont été sauvegardés dans 'valides_codes_nitro.txt'.")

def id_to_token():
    print(" [ID TO TOKEN]")
    userid = input(" [INPUT] USER ID : ")
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print(f'\n [LOGS] TOKEN FIRST PART : {encodedStr}')
    os.system('pause >nul')  # Pause pour maintenir la fenêtre ouverte

# Autres fonctions de votre outil ici...

# Menu principal
def main_menu():
    while True:
        print(themain)
        choice = input("Veuillez choisir une option (1-10) ou 'q' pour quitter : ").strip()
        
        if choice == '1':
            toolinfo()
        elif choice == '2':
            ip_lookup()
        elif choice == '3':
            ip_generator()
        elif choice == '4':
            gmail_generator()
        elif choice == '5':
            print(get_my_ip())
        elif choice == '6':
            password_hashing()
        elif choice == '7':
            site_cloner()
        elif choice == '8':
            webhook_spammer()
        elif choice == '9':
            nitro_generator()
        elif choice == '10':
            id_to_token()  # Option 10 pour récupérer la première partie du token
        elif choice.lower() == 'q':
            print("Merci d'avoir utilisé SARGI tool !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main_menu()
