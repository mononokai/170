from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# # Creating a random byte string to be used as a key
# simple_key = get_random_bytes(32)
# print(simple_key)


salt = b'\x8c\xf2"y\x15\xb6\xd8=\xbb<\xdb\x15\xde%%\xd5k\xac\xd0\xbfj\xa8\xc7\xc5\x87D\x1e)\xf7\xd3\x14\xd9'
password = 'pass123'

key = PBKDF2(password, salt, dkLen=32)
# print(key)


# message = b"Hello Secret World!"
message = input("Enter the message to encrypt: ").encode()

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

# with open('encrypted.bin', 'rb') as f:
#     iv = f.read(16)
#     decrypt_data = f.read()

# cipher = AES.new(key, AES.MODE_CBC, iv=iv)
# original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
# print(original)

with open ('key.bin', 'wb') as f:
    f.write(key)