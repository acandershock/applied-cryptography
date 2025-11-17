"""
If hashing a string: encode to bytes using ASCII
If hashing a number: encode to bytes in big-endian
"""

import math
import binascii
import random
from hashlib import sha256

# covert string to ascii (bytes)
def string_to_bytes(s: str):
    return s.encode('ascii')

# convert int to bytes
def int_to_bytes(i: int):
    length = math.ceil(i.bit_length() / 8)
    return i.to_bytes(length, byteorder='big', signed=False)

# convert bytes (hex) to int
def bytes_to_int(data: bytes):
    return int.from_bytes(data, 'big')

# convert bytes to hex string
def bytes_to_hex(data: bytes):
    hex_bytes = binascii.hexlify(data)
    return hex_bytes.decode('ascii')

# convert hex string to bytes
def hex_to_bytes(hex_string: str):
    return bytes.fromhex(hex_string)

def generate_nonce():
    a = random.randint(0, 2**31-1)
    return a

def generate_hash(previous_block_hash, nonce, quote):
    previous_block_bytes = hex_to_bytes(previous_block_hash)
    nonce_bytes = int_to_bytes(nonce)
    quote_bytes = string_to_bytes(quote)
    byte_string = previous_block_bytes + nonce_bytes + quote_bytes
    hash = bytes_to_hex(sha256(byte_string).digest())
    return hash

def hash_24(previous_block_hash, quote, difficulty_parameter):
    zeros = difficulty_parameter // 4
    counter = 0

    while True:
        nonce = generate_nonce()
        hash = generate_hash(previous_block_hash, nonce, quote)
        counter += 1
        print(f"counter: {counter}")

        if (hash.startswith('0' * zeros)):
            print(f"total counter: {counter}")
            print(f"nonce: {nonce}")
            print(f"hash: {hash}")
            return nonce, hash