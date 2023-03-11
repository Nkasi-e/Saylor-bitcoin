import hashlib

my_string = 'cryptography is fun'

print(f'My string is: {my_string}')

my_hash = hashlib.sha256(my_string.encode())

print(f'My SHA256 hash is: {my_hash.hexdigest()}')

print('The length of your hash is:', len(my_hash.hexdigest()))
