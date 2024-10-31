from colorama import Fore, init
import requests
import random
import time
import os
from urllib.parse import urlparse
import hashlib
import string
import base64

# Initialize colorama
init(autoreset=True)

# Default global color variable (Blue)
color = Fore.BLUE

# Function to print with the global color
def colored_print(text):
    global color
    print(color + text)

# Function to display the banner with dynamic color
def print_banner():
    colored_print("""
                                        ██████  ▄▄▄       ██▀███    ▄████  ██▓
                                      ▒██    ▒ ▒████▄    ▓██ ▒ ██▒ ██▒ ▀█▒▓██▒
                                      ░ ▓██▄   ▒██  ▀█▄  ▓██ ░▄█ ▒▒██░▄▄▄░▒██▒
                                        ▒   ██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█  ██▓░██░
 [!] Settings                         ▒██████▒▒ ▓█   ▓██▒░██▓ ▒██▒░▒▓███▀▒░██░     [+] https://discord.gg/4Dz78Dym
 [Q] Leave                           ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ░▒   ▒ ░▓  
                                     ░ ░▒  ░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░  ░   ░  ▒ ░
                                      ░  ░  ░    ░   ▒     ░░   ░ ░ ░   ░  ▒ ░
                                             ░        ░  ░   ░           ░  ░  
                                                                                           
╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                     ═══╗
║   [01] > Tool Info                 ║ ║ [05] > Check Your IP                ║ ║ [09] > Nitro Generator    ║
║   [02] > IP Lookup                 ║ ║ [06] > Hash Password                ║ ║ [10] > ID TO TOKEN        ║
║   [03] > Generate IP               ║ ║ [07] > Clone Site [SCRAPPER]        ║ ║ [11] > Generator          ║
║   [04] > Generate Email            ║ ║ [08] > Spam Webhook                 ║ ║ [12] > Dmall Friend       ║
╚═══                              ═══╝ ╚═══                               ═══╝ ╚═══                     ═══╝
""")

def display_tool_info():
    info = ("Multitool with several features to facilitate various processes.")
    print(info)

def retrieve_my_ip():
    try:
        response = requests.get('https://api.ipify.org/')
        if response.status_code == 200:
            return (f"Your IP address is: {response.text.strip()}")
    except:
        return ("Error retrieving your IP address.")

def lookup_ip():
    ip_address = input("Enter the IP address: ")
    result = check_ip(ip_address)
    print(result)

def generate_random_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def check_ip(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        return (f"{ip_address} ✅") if response.status_code == 200 else (f"{ip_address} ❌")
    except Exception as e:
        return (f"Error checking IP: {str(e)}")

def generate_ips():
    num_ips = int(input("How many IP addresses do you want to generate? : "))
    for _ in range(num_ips):
        print(check_ip(generate_random_ip()))
        time.sleep(1)  

def generate_email():
    return f"user{random.randint(1000, 9999)}@{random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'])}"

def check_email(email_address):
    return (f"{email_address} ✅")

def gmail_generator():
    num_emails = int(input("How many Gmail addresses do you want to generate? : "))
    for _ in range(num_emails):
        print(check_email(generate_email()))
        time.sleep(1)

def hash_password():
    password = input("Enter the password to hash: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print(f"Hashed password: {hashed_password}")

def clone_website():
    url = input("Enter the URL of the site to clone: ")
    site_name = urlparse(url).netloc.replace("www.", "")
    folder_name = site_name

    os.makedirs(folder_name, exist_ok=True)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(folder_name, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"The site {url} has been cloned into the folder '{folder_name}/index.html'.")
        else:
            print(f"Error retrieving the site. Status: {response.status_code}")
    except Exception as e:
        print(f"Error cloning: {str(e)}")

def send_webhook_spam():
    url = input("Enter the webhook URL: ").strip()
    message = input("Message to send: ").strip()
    num_messages = int(input("Number of times to send: ").strip())
    payload = {"content": message}

    print("Sending messages...")
    for _ in range(num_messages):
        response = requests.post(url, json=payload)
        if response.status_code == 204:
            print("Message sent.")
        else:
            print(f"Send error: Code {response.status_code}")
        time.sleep(1)

def generate_nitro_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def generate_nitro_codes():
    url = input("Enter the Discord webhook URL: ").strip()
    num_codes = int(input("Number of Nitro codes to generate: ").strip())

    codes = [f"https://discord.gift/{generate_nitro_code()}" for _ in range(num_codes)]
    with open("valid_nitro_codes.txt", "w") as f:
        for code in codes:
            response = requests.post(url, json={"content": code})
            if response.status_code == 204:
                print(f"Code sent: {code}")
                f.write(code + "\n")
            else:
                print(f"Send error: {code} - Status: {response.status_code}")
            time.sleep(1)

    print("Valid codes saved in 'valid_nitro_codes.txt'.")

def id_to_token():
    userid = input("Enter the user ID: ")
    encoded = base64.b64encode(userid.encode("utf-8")).decode("utf-8")
    print(f'Token (first part): {encoded}')
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

    print("Available gift card options:")
    for key, value in options.items():
        print(f"[{key}] Gift card generator for {value}")

    choice = input("Choose an option (1-7) to generate a gift card: ").strip()
    if choice in options:
        num_cards = int(input(f"How many {options[choice]} gift cards do you want to generate? : ").strip())
        
        valid_codes = []
        for _ in range(num_cards):
            # Generate a fictitious gift card code
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
            valid_codes.append(code)

        print(f"Generated {num_cards} {options[choice]} gift cards:")
        for code in valid_codes:
            print(code)
    else:
        print("Invalid choice. Please try again.")

# Main function
if __name__ == "__main__":
    while True:
        print_banner()
        choice = input("Choose an option: ")
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
        elif choice == '11':
            generate_gift_card()
        elif choice == '12':
            print("Exiting...") 
            break
        else:
            print("Invalid option, please choose again.")
