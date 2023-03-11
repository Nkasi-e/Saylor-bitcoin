from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify


"""
This exercise is to encrypt and decrypt data
using the RSA algorithm of public keys and private keys
"""

message = b'bitcoin is going to be fun with cryptography'

private_key = RSA.generate(1024)
public_key = private_key.publickey()

print(type(private_key), type(public_key))

# Now we'll convert our keys to strings, save them in.pem files and take a look at them.
private_pem = private_key.export_key().decode()
public_pem = public_key.export_key().decode()


print(type(private_pem), type(public_pem))


# Saving the string to .pem file
with open('private.pem', 'w') as pr:
    pr.write(private_pem)
with open('public.pem', 'w') as pu:
    pu.write(public_pem)

# Print
print('private.pem:')
with open('private.pem', 'r') as f:
    print(f.read())

print('public.pem:')
with open('public.pem', 'r') as f:
    print(f.read())

# Converting these key file back into RSA key objects and do some encrypting
pr_key = RSA.import_key(open('private.pem', 'r').read())
pu_key = RSA.import_key(open('public.pem', 'r').read())

print(type(pr_key), type(pu_key))


# Encrypting
cipher = PKCS1_OAEP.new(key=pu_key)
cipher_text = cipher.encrypt(message)


print(f'encrypted message: {cipher_text}')

# Using private key to decrypt the message
decrypt = PKCS1_OAEP.new(key=pr_key)
decrypt_message = decrypt.decrypt(cipher_text)


# Print decrypted message
print(f'decrypted message: {decrypt_message}')

print("Done!")
