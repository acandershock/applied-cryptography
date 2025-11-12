"""
If hashing a string: encode to bytes using ASCII
If hashing a number: encode to bytes in big-endian
"""

import math
import binascii

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
    return bytearray.fromhex(hex_string)

# mod exponentiation
def fast_modular_exponentiation(b: int, e: int, n: int) -> int:
    binary_string = format(e, 'b')[::-1]
    product = 1

    # iterate through length of e
    for binary_char in binary_string:
        e_i = int(binary_char)

        if e_i == 1:
            product = ((product * b) % n)
        
        b = ((b * b) % n)
    
    return product