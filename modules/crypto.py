"""
Spider-C2 Module : Crypto
AES encryption/decryption for C2 communication.
"""

import base64
import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class C2Crypto:
    def __init__(self, key):
        self.key = self._derive_key(key)

    def _derive_key(self, password):
        return hashlib.sha256(password.encode()).digest()

    def encrypt(self, plaintext):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padded = plaintext + (16 - len(plaintext) % 16) * chr(16 - len(plaintext) % 16)
        ciphertext = encryptor.update(padded.encode()) + encryptor.finalize()
        return base64.b64encode(iv + ciphertext).decode()

    def decrypt(self, ciphertext):
        raw = base64.b64decode(ciphertext)
        iv = raw[:16]
        ciphertext = raw[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded = decryptor.update(ciphertext) + decryptor.finalize()
        plaintext = padded[:-padded[-1]]
        return plaintext.decode()
