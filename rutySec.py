import secrets
import string
import os
import hashlib
import requests
from cryptography.fernet import Fernet
from subprocess import check_output, run
from colorama import Fore, Style
import art

HIBP_API = "https://api.pwnedpasswords.com/range/"
ROCKYOU_PATH = "rockyou.txt"  

def generate_key(key_file="key.key"):
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as file:
            file.write(key)

def load_key(key_file="key.key"):
    if os.path.exists(key_file):
        with open(key_file, "rb") as file:
            return file.read()
    else:
        raise FileNotFoundError("Encryption key not found. Run the program again to generate it.")

def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()

def generate_password(length=20):
    char_pool = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(char_pool) for _ in range(length))

def hash_password(password, algo="sha256"):
    if algo.lower() == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algo.lower() == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif algo.lower() == "sha512":
        return hashlib.sha512(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hashing algorithm")

def check_password_pwned(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    response = requests.get(HIBP_API + prefix)
    if suffix in response.text:
        print(f"{Fore.RED}[!] This password has been leaked!{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}[+] Password not found in leaks.{Style.RESET_ALL}")

def dictionary_attack(target_hash, algo="sha256"):
    if not os.path.exists(ROCKYOU_PATH):
        print(f"{Fore.RED}[!] RockYou.txt file not found!{Style.RESET_ALL}")
        return
    
    print(f"{Fore.YELLOW}[*] Running dictionary attack...{Style.RESET_ALL}")
    with open(ROCKYOU_PATH, "r", errors="ignore") as file:
        for word in file:
            word = word.strip()
            if hash_password(word, algo) == target_hash:
                print(f"{Fore.GREEN}[+] Password cracked: {word}{Style.RESET_ALL}")
                return
    print(f"{Fore.RED}[-] No match found.{Style.RESET_ALL}")

def main():
    generate_key()
    key = load_key()
    
    print(Fore.RED + art.text2art("RUTYSec") + Style.RESET_ALL)
    print(Fore.BLUE + "[+] Creator: C4l3bpy\n" + Fore.WHITE)
    
    while True:
        print(Fore.YELLOW + "\nOptions:" + Style.RESET_ALL)
        print("1. Generate a Secure Password")
        print("2. Hash a Password")
        print("3. Check if Password is Leaked")
        print("4. Run Dictionary Attack")
        print("5. Exit")
        choice = input(Fore.CYAN + "Select an option: " + Style.RESET_ALL)
        
        if choice == "1":
            password = generate_password()
            print(f"Generated Password: {Fore.GREEN}{password}{Style.RESET_ALL}")
        elif choice == "2":
            password = input("Enter password to hash: ")
            algo = input("Enter hashing algorithm (md5, sha256, sha512): ")
            print(f"Hashed Password: {Fore.GREEN}{hash_password(password, algo)}{Style.RESET_ALL}")
        elif choice == "3":
            password = input("Enter password to check: ")
            check_password_pwned(password)
        elif choice == "4":
            target_hash = input("Enter target hash: ")
            algo = input("Enter hashing algorithm (md5, sha256, sha512): ")
            dictionary_attack(target_hash, algo)
        elif choice == "5":
            break
        else:
            print(f"{Fore.RED}Invalid option. Try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()