import key
import random
from hashlib import sha256

# 1. Log into pass-off server
g = 5
p = 233000556327543348946447470779219175150430130236907257523476085501968599658761371268535640963004707302492862642690597042148035540759198167263992070601617519279204228564031769469422146187139698860509698350226540759311033166697559129871348428777658832731699421786638279199926610332604408923157248859637890960407

# 2a. Generate random int 'a'
a = random.randint(1_000_000, 9_999_999)
print(f"a: {a}\n")
a = 7184035

# 2b. Calculate public key, g^a (mod p)
A = key.fast_modular_exponentiation(g, a, p)
print(f"A: {A}\n")

# 3. Calculate the shared key
net_id = "aandersh"
password = "cubicular"
salt_hex = "6bcf0ca2"
iterations = 1_000
B_hat = 189641380557702472320032568264970926991792224569375559544567730087298532926947079208338843159633183326521207532169144708290280209637791005198672793628284052064970869522651113462466914750655075852498670953691780146619297554260220635984362851853109501264006021053621680698579658776226126021978454468425280637117

# 3a. x = H(salt || password)^1000

salt_bytes = key.hex_to_bytes(salt_hex)
password_bytes = key.string_to_bytes(password)
byte_string = salt_bytes + password_bytes

x = sha256(byte_string) # initialize
for _ in range(999):
    x = sha256(x.digest())

x = key.bytes_to_int(x.digest())
print(f"x: {x}\n")

# 3b. Calculate public key, g^b
# k = H (p || g) as an int
g_bytes = key.int_to_bytes(g)
p_bytes = key.int_to_bytes(p)
byte_string = p_bytes + g_bytes
k = key.bytes_to_int(sha256(byte_string).digest())
print(f"k: {k}\n")

# g^b = B_hat - k * g^x (mod p)
v = key.fast_modular_exponentiation(g, x, p)
B = (B_hat - k*v) % p
print(f"B: {B}\n")

# 3c. Calculate u
# u = H(A || B)
A_bytes = key.int_to_bytes(A)
B_bytes = key.int_to_bytes(B)
byte_string = A_bytes + B_bytes
u = key.bytes_to_int(sha256(byte_string).digest())
print(f"u: {u}\n")

# 3d. Calculate shared key
shared_key = key.fast_modular_exponentiation(B, a+u*x, p)
print(f"shared key: {shared_key}\n")

# 4. Calculate M1
# M1 = H (H(p) XOR H(g) || H(net_id) || salt || A || B || shared_key)
hash_p = key.bytes_to_int(sha256(p_bytes).digest())
hash_g = key.bytes_to_int(sha256(g_bytes).digest())
hash_int = hash_p ^ hash_g
hash_bytes = key.int_to_bytes(hash_int)
hash_id = (sha256(key.string_to_bytes(net_id))).digest()
shared_key_bytes = key.int_to_bytes(shared_key)
byte_string = hash_bytes + hash_id + salt_bytes + A_bytes + B_bytes + shared_key_bytes
M1 = key.bytes_to_hex(sha256(byte_string).digest())
print(f"M1: {M1}\n")

# Calculate M2
# M2 = H(A || M1 || shared_key)
M1_bytes = key.hex_to_bytes(M1)
byte_string = A_bytes + M1_bytes + shared_key_bytes
M2 = key.bytes_to_hex(sha256(byte_string).digest())
print(f"M2: {M2}\n")