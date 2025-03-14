import secrets
import string
from cryptography.fernet import Fernet
def generatePassword(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

password = generatePassword(16)
key = Fernet.generate_key()
fernet = Fernet(key)

encrypted_password = fernet.encrypt(password.encode())

with open('password.txt', 'wb') as file:
    file.write(encrypted_password)
    
print(f'Password: {password}')
print(f'key: {key.decode()}')
print(f'Encrypted password: {encrypted_password.decode()}')