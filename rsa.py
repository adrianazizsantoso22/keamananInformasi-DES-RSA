import random
from math import gcd

class RSA:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def encrypt(self, message, public_key):
        e, n = public_key
        encrypted_message = [pow(ord(char), e, n) for char in message]
        return encrypted_message
    
    def decrypt(self, encrypted_message):
        d, n = self.private_key
        decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
        return decrypted_message

    def generate_rsa_keys(self):
        p = self.generate_prime_number()
        q = self.generate_prime_number()
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randint(1, phi)
        while gcd(e, phi) != 1:
            e = random.randint(1, phi)
        d = self.mod_inverse(e, phi)
        self.private_key = (d, n)
        self.public_key = (e, n)

    def generate_prime_number(self):
        while True:
            prime = random.randint(100, 1000)
            if self.is_prime(prime):
                return prime

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def mod_inverse(self, e, phi):
        d = 0
        x1, x2, y1, y2 = 0, 1, 1, 0
        while e > 0:
            q = phi // e
            e, phi = phi % e, e
            x1, x2 = x2 - q * x1, x1
            y1, y2 = y2 - q * y1, y1
        return x2 + phi if phi < 0 else x2
