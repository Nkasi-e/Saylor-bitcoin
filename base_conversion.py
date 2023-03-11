"""
converting data with base58
"""

import base58


my_string = b"Hello people"

my_base58 = base58.b58encode(my_string)

print(f'Base58 encoded string: {my_base58}')


decode_base58 = base58.b58decode(my_base58)

print(f'Decoded base58 encoded string: {decode_base58}')

"""
hex conversion
"""
my_num = 57

hex_num = hex(my_num)

print(f'Hexadecimal number: {hex_num}')
