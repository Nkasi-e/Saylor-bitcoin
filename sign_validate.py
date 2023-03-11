from ecdsa import SigningKey, SECP256k1

"""
Sign and validate data using the elliptic curve algorithm
"""

# Note that here is where we are specifying which curve to use, Secp256k1
sk = SigningKey.generate(curve=SECP256k1)

print(f'origin: {sk}')

# And our public, or verifying, key…
vk = sk.verifying_key

print(f'first: {vk}')

# Next, we'll need a message to sign. In this script, you can use whatever string you'd like, but just for fun, we'll use a crypto classic here.
signature = sk.sign(b"Not your keys, not your coins!")

print(f'signature: {signature}')

assert vk.verify(signature, b"Not your keys, not your coins!")

print("If your script runs to this point without an error, congrats, you successfully validated the signature!")
