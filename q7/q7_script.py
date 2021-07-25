import sys
import hashlib
import string
import secrets
salt_length = 20
alphabet = string.ascii_letters + string.digits
salt = bytes(''.join(secrets.choice(alphabet) for i in range(salt_length)),'utf-8')
try:
    password = bytes(str(sys.argv[1]),'utf-8')
    hash = hashlib.pbkdf2_hmac(hash_name='sha512',password=password,salt=salt,iterations=200000)
    print(hash.hex())
except IndexError:
    print("Please provide a password for hashing")
