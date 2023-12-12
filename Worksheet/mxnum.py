import math
from fraction import Fraction
# class Mixed_fraction:
#     def __init__(self, W_n, numerator, denominator):
#         if numerator < denominator:
#             hcf = math.gcd(numerator, denominator)
#             self.W_n = W_n
#             self.numerator = numerator // hcf
#             self.denominator = denominator // hcf
#         else:
#             hcf = math.gcd((numerator % denominator), denominator)
#             self.W_n = W_n +(numerator//denominator)
#             self.numerator = (numerator % denominator)//hcf
#             self.denominator = denominator//hcf
class Mixed_fraction:
    def __init__(self, W_n, numerator, denominator):
        hcf = math.gcd(numerator, denominator)
        self.numerator = numerator//hcf
        self.denominator = denominator // hcf

        self.W_n = W_n + numerator // denominator
        self.numerator = self.numerator % self.denominator
    def __repr__(self):
        if self.numerator == 0:
            return str(self.W_n)
        return str(self.W_n) + ' ' + str(self.numerator) + '/' + str(self.denominator)
    def __eq__(self, other):
        return self.W_n == other.W_n and self.numerator == other.numerator and self.denominator == other.denominator
    def __mul__(self, other):
        return Mixed_fraction(self.W_n*other.W_n, self.numerator*other.numerator, self.denominator*other.denominator)
    def __add__(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        numer1 = (lcm // self.denominator) * self.numerator
        numer2 = (lcm // other.denominator) * other.numerator
        return Mixed_fraction(self.W_n + other.W_n, numer1+numer2, lcm)
    def __sub__(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        numer1 = (lcm // self.denominator) * self.numerator
        numer2 = (lcm // other.denominator) * other.numerator
        return Mixed_fraction(self.W_n - other.W_n, numer1 - numer2, lcm)
    def __iadd__(self, other):
        return self + other
    def __isub__(self, other):
        return self - other
    def __truediv__(self, other):
        fract1 = Fraction(self.W_n * self.denominator + self.numerator, self.denominator)
        fract2 = Fraction(self.W_n * self.denominator + self.numerator, self.denominator)
        fract3 = fract1 / fract2
        return Mixed_fraction(0, fract3.numerator, fract3.denominator)