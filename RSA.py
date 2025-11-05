import math
from pprint import pprint
from string import ascii_lowercase

encoding = {c: ascii_lowercase.index(c) + 1 for c in ascii_lowercase}
encoding[" "] = 27

def extended_euclid(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = extended_euclid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y

def modinv(a, m):
    d, x, _ = extended_euclid(a, m)
    if d != 1:
        return None
    return x % m

def rsa_gen_public_private_keys(p, q):
    phi = (p - 1) * (q - 1)
    e = 3
    while e < phi:
        if math.gcd(e, phi) == 1:
            break
        e += 2
    d = modinv(e, phi)
    return e, d

def rsa_encrypt(message, n, e):
    return pow(message, e, n)

def rsa_decrypt(encrypted, n, d):
    return pow(encrypted, d, n)

def encode(message):
    encoded = ""
    for c in message:
        i = encoding[c]
        encoded += f"{i:02d}"
    return int(encoded)

def decode(int_message):
    s = str(int_message)
    if len(s) % 2 != 0:
        s = "0" + s
    decoded = ""
    for i in range(0, len(s), 2):
        num = int(s[i:i+2])
        for k, v in encoding.items():
            if v == num:
                decoded += k
    return decoded

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gen_big_prime_less_than(upper_bound):
    for i in range(upper_bound, 1, -1):
        if is_prime(i):
            return i
    return None

def split_into_smaller_messages(message, n):
    s = str(message)
    size = len(str(n)) - 1
    return [int(s[i:i+size]) for i in range(0, len(s), size)]

def have_fun_rsa(upper_bound, message):
    p = gen_big_prime_less_than(upper_bound)
    q = gen_big_prime_less_than(p)
    e, d = rsa_gen_public_private_keys(p, q)
    n = p * q
    encoded = encode(message)
    if encoded > n:
        parts = split_into_smaller_messages(encoded, n)
        for part in parts:
            enc = rsa_encrypt(part, n, e)
            dec = rsa_decrypt(enc, n, d)
            dec_msg = decode(dec)
            pprint((part, enc, dec, dec_msg))
    else:
        enc = rsa_encrypt(encoded, n, e)
        dec = rsa_decrypt(enc, n, d)
        pprint((encoded, enc, dec, decode(dec)))

have_fun_rsa(1000, "Ritik is eating bread")
