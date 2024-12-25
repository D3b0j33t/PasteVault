from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
encryption_key = os.getenv("ENCRYPTION_KEY")

if not encryption_key:
    raise ValueError("Missing ENCRYPTION_KEY in environment variables")

# Initialize Fernet cipher suite
cipher_suite = Fernet(encryption_key)

def encrypt_text(plain_text):
    """
    Encrypt a string using Fernet encryption.
    """
    return cipher_suite.encrypt(plain_text.encode()).decode()

def decrypt_text(encrypted_text):
    """
    Decrypt a string using Fernet encryption.
    """
    return cipher_suite.decrypt(encrypted_text.encode()).decode()
