import sys
import hashlib
try:
    password = bytes(str(sys.argv[1]),'utf-8')
    hash = hashlib.pbkdf2_hmac(hash_name='sha512',password=password,salt=b'Km5d5ivMy8iexuHcZrsD',iterations=200000)
    print(hash.hex())
except IndexError:
    print("Please provide a password for hashing")
