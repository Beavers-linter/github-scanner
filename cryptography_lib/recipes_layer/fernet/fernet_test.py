"""
Fernet guarantees that a message encrypted using it cannot be manipulated
or read without the key. Fernet is an implementation of symmetric
(also known as “secret key”) authenticated cryptography.
"""
import time

# from datetime import time

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"my deep dark secret")
print("encrypt", token)
token2 = f.encrypt_at_time(b"my deep dark secret", int(time.time()))
print("encrypt_at_time", token2)
f.decrypt(token)  # decrypt(token, ttl=None)
f.decrypt_at_time(token, 1000, int(time.time()))
print(f.extract_timestamp(token))