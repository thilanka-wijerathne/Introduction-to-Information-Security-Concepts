import sys
import hashlib
import string
import secrets
salt_length = 20
alphabet = string.ascii_letters + string.digits
salt = ''.join(secrets.choice(alphabet) for i in range(salt_length))
try:
    password = str(sys.argv[1])
    salted_password = salt+password
    hash = hashlib.sha512(salted_password.encode())
    print(hash.hexdigest())
except IndexError:
    print("Please provide a password for hashing")
