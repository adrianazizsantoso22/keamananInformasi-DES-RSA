import random
from math import gcd

class RSA:
    def __init__(self):
        """Inisialisasi objek RSA tanpa kunci privat atau publik."""
        self.private_key = None
        self.public_key = None

    def random_print(self):
        """Mencetak pesan sederhana untuk memastikan program berjalan."""
        print("Hello, World! ini dari rsa.py")
    
    def encrypt(self, message, public_key):
        """Mengenskripsi pesan menggunakan kunci publik.
        
        Args:
            message (str): Pesan yang akan dienkripsi.
            public_key (tuple): Kunci publik (e, n).
        
        Returns:
            list: Pesan terenkripsi dalam bentuk angka.
        """
        e, n = public_key
        encrypted_message = [pow(ord(char), e, n) for char in message]
        return encrypted_message
    
    def decrypt(self, encrypted_message):
        """Mengdekripsi pesan menggunakan kunci privat.
        
        Args:
            encrypted_message (list): Pesan terenkripsi.
        
        Returns:
            str: Pesan yang telah didekripsi.
        """
        d, n = self.private_key
        decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
        return decrypted_message
    
    def is_prime(self, num):
        """Memeriksa apakah angka adalah bilangan prima.
        
        Args:
            num (int): Angka yang akan diperiksa.
        
        Returns:
            bool: True jika angka adalah prima, False jika tidak.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_prime_number(self):
        """Menghasilkan bilangan prima acak antara 100 dan 1000.
        
        Returns:
            int: Bilangan prima yang dihasilkan.
        """
        while True:
            prime = random.randint(100, 1000)
            if self.is_prime(prime):
                return prime

    def generate_rsa_keys(self):
        """Menghasilkan kunci RSA (kunci publik dan privat).
        
        Proses ini melibatkan pemilihan dua bilangan prima p dan q,
        menghitung n dan phi, serta memilih e dan d yang sesuai.
        """
        p = self.generate_prime_number()
        q = self.generate_prime_number()

        n = p * q
        phi = (p - 1) * (q - 1)

        e = random.randint(1, phi)
        while gcd(e, phi) != 1:
            e = random.randint(1, phi)

        d = 0
        while (d * e) % phi != 1:
            d += 1

        self.private_key = (d, n)
        self.public_key = (e, n)