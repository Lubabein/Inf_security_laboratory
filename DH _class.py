import primesieve
import random


class User:
    def __init__(self, secret_num, p, g):
        self.p = p
        self.g = g
        self.secret_num = secret_num
        self.key = pow(g, secret_num) % p

    def get_key(self):
        return self.key

    def get_secret_key(self, companion_key):
        return pow(companion_key, self.secret_num) % self.p


g = primesieve.nth_prime(random.randint(50, 150))#257
p = primesieve.nth_prime(random.randint(50, 150))#23
Naruto = User(random.randint(1, 500), p, g)
Sasuke = User(random.randint(1, 500), p, g)
print('Natuto key:', Naruto.get_secret_key(Sasuke.get_key()))
print('Sasuke key:', Sasuke.get_secret_key(Naruto.get_key()))
